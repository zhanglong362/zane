# -*- encoding: utf-8 -*-

import os
from lib import utils
from conf import settings
from functools import wraps

CURRENT_USER = None
COOKIES = {}
SHOPPING_CART = {}
logger = utils.get_logger('shopping')

def auth(func):
    '''
    auth decorator to user authentication.
    :param func: function name
    :return: function or fail error
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        name = CURRENT_USER
        if not name or name not in COOKIES:
            logger.warning('用户%s没有登录，请您先登录！' % name)
            login()
        else:
            return func(*args, **kwargs)
    return wrapper

def logout(func):
    '''
    logout decorator to user logout from shopping mall.
    :param func: function name
    :return: return string and exit shopping mall
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        name = CURRENT_USER
        result = func(*args, **kwargs)
        if result == 'quit':
            if name in SHOPPING_CART:
                params = {
                    'mode': 'w',
                    'file_path': settings.SHOPPING_CART_FILE % name,
                    'data': SHOPPING_CART.pop(name)
                }
                utils.file_handler(**params)
            if name:
                logger.info('用户%s退出登录成功！' % name)
            else:
                logger.info('程序退出登录成功！')
            os._exit(0)
        elif result == 'order':
            logger.info('请您进入购物车确认商品，并下单支付！')
            run()
        else:
            return result
    return wrapper

@logout
def input_string(word, name=None, register=None):
    '''
    Function input_string to return a string type object.
    :param word: tips word
    :param password: if pasword True return string, else check string isalpha and return
    :return: string
    '''
    while True:
        string = input('%s >>: ' % word).strip()
        if string in ['quit', 'order']:
            return string
        if name and not string.isalpha():
            print('用户名只能是字母！')
            continue
        if register:
            password = input('再次输入%s >>: ' % word).strip()
            if password in ['quit', 'order']:
                return password
            if string != password:
                logger.warning('两次输入密码不一致！')
                continue
            return string
        return string

@logout
def input_number(word):
    '''
    Function input_number to return a number type object.
    :param word: tips word
    :return: a number type object
    '''
    while True:
        number = input('%s >>: ' % word).strip()
        if not number.isdigit():
            continue
        number = int(number)
        return number

def register(credit_limit=50000):
    '''
    Funtion register to user register
    :param credit_limit: user's credit limit
    :return: True or None
    '''
    name = input_string('用户名', name=True)
    if utils.checkpath(settings.USER_FILE % (name, name)):
        logger.warning('用户%s已经注册，请直接登陆！' % name)
        return
    password = input_string('密码', register=True)
    params = {
        'file_path': settings.USER_FILE % (name, name),
        'mode': 'w',
        'data': {
            'name': name,
            'password': password,
            'permission': 'user',             # admin: 管理员  user: 普通用户
            'status': 0,                      # 0：正常 1: 锁定用户
            'balance': 0,
            'credit_balance': credit_limit,
            'credit_limit': credit_limit,     # 0 冻结
            'bill': 0
        }
    }
    if utils.file_handler(**params):
        logger.info('用户%s注册成功！' % name)
        return True

def load_user_shopping_cart(name):
    '''
    Function load_user_shopping_cart to print shopping cart info
    :param name: user's name
    :return: True or None
    '''
    file_path = settings.SHOPPING_CART_FILE % name
    params = {
        'mode': 'r',
        'file_path': file_path
    }
    if os.path.exists(file_path):
        SHOPPING_CART[name] = utils.file_handler(**params)
        return True
    else:
        SHOPPING_CART[name] = {}

def login():
    '''
    Function login to login shopping mall
    :return: True or None
    '''
    global CURRENT_USER, COOKIES
    while True:
        name = input_string('用户名', name=True)
        if not utils.checkpath(settings.USER_FILE % (name, name)):
            logger.warning('用户%s没有注册，请您先注册！' % name)
            break
        if name in COOKIES:
            logger.info('用户%s已经是登陆状态！' % name)
            CURRENT_USER = name
            return True
        password = input_string('密码')
        params = {
            'file_path': settings.USER_FILE % (name, name),
            'mode': 'r'
        }
        user_info = utils.file_handler(**params)
        if password != user_info['password']:
            logger.warning('用户%s密码错误！' % name)
            continue
        logger.info('用户%s登陆成功！' % name)
        CURRENT_USER = name
        COOKIES[name] = {
            'balance': user_info['balance'],
            'credit_balance': user_info['credit_balance'],
            'credit_limit': user_info['credit_limit'],
            'bill': user_info['bill']
        }
        load_user_shopping_cart(name)
        return True

def get_goods_info(output=None):
    '''
    Function get_goods_info to return goods information.
    :param output: print or not print to console
    :return: goods information
    '''
    params = {
        'mode': 'r',
        'file_path': settings.GOODS_FILE
    }
    goods = utils.file_handler(**params)
    if output:
        print('=' * 30)
        print('商品编号    商品名称    商品价格 [order下单]')
        for k, v in goods.items():
            print('%-10s %-10s %-10s' % (k, v['name'], v['price']))
        print('=' * 30)
    return goods

@auth
def shopping():
    '''
    Function shopping to user's shopping
    :return: None or exit (when order)
    '''
    global COOKIES, SHOPPING_CART
    balance = COOKIES[CURRENT_USER]['balance']
    credit_balance = COOKIES[CURRENT_USER]['credit_balance']
    credit_limit = COOKIES[CURRENT_USER]['credit_limit']
    while True:
        goods = get_goods_info(output=True)
        code = input_string('请输入商品编码')
        if code not in goods:
            logger.warning('输入商品编号非法！')
            continue
        good = goods[code]['name']
        price = goods[code]['price']
        count = input_number('请输入商品数量')
        cost = price * count
        if balance >= cost or credit_balance >= cost:
            if good not in SHOPPING_CART[CURRENT_USER]:
                SHOPPING_CART[CURRENT_USER][good] = {
                    'code': code,
                    'price': price,
                    'count': count
                }
            else:
                SHOPPING_CART[CURRENT_USER][good]['count'] += count
        if balance >= cost:
            balance -= cost
            COOKIES[CURRENT_USER]['balance'] = balance
        elif balance < cost and credit_balance >= cost:
            if credit_limit == 0:
                logger.warning('用户%s信用卡已冻结，无法使用信用卡购物！' % CURRENT_USER)
                return
            credit_balance -= cost
            COOKIES[CURRENT_USER]['credit_balance'] = credit_balance
            logger.info('用户%s使用信用卡支付！' % CURRENT_USER)
        else:
            diff = cost - (balance + credit_balance)
            logger.info('账户余额: %s 信用卡余额: %s 购买商品 %s x %s 还需 %s' % (balance, credit_balance, good, count, diff))
            return
        logger.info('账户余额: %s 信用卡余额: %s 购物车: %s \n' % (balance, credit_balance, SHOPPING_CART[CURRENT_USER]))

def print_shopping_cart():
    '''
    Funciton print_shopping_cart to print shopping cart
    :return: goods total cost in shopping cart
    '''
    cost = 0
    print('=' * 50)
    print('商品名称    商品编号    商品价格    商品数量    [输入order下单]\n')
    for k, v in SHOPPING_CART[CURRENT_USER].items():
        good, code, price, count = k, v['code'], v['price'], v['count']
        print('%-10s %-10s %-10s %-10s' % (good, code, price, count))
        cost += (price * count)
    print('\n商品总价: %s' % cost)
    print('账户余额: %s' % COOKIES[CURRENT_USER]['balance'])
    print('信用卡余额: %s' % COOKIES[CURRENT_USER]['credit_balance'])
    print('=' * 50)
    return cost

def edit_shopping_cart():
    '''
    Function edit_shopping_cart to delete good in shopping cart
    :return: None
    '''
    global COOKIES, SHOPPING_CART
    while True:
        balance = COOKIES[CURRENT_USER]['balance']
        credit_balance = COOKIES[CURRENT_USER]['credit_balance']
        credit_limit = COOKIES[CURRENT_USER]['credit_limit']
        goods = get_goods_info()
        print_shopping_cart()
        code = input_string('请输入要删除的商品编码')
        if code not in goods:
            logger.warning('输入商品编号非法！')
            continue
        good = goods[code]['name']
        price = goods[code]['price']
        if good not in SHOPPING_CART[CURRENT_USER]:
            logger.warning('购物车内无此商品: %s' % good)
            continue
        count = input_number('请输入要删除的商品数量')
        if count > SHOPPING_CART[CURRENT_USER][good]['count']:
            logger.warning('删除的数量，不能大于购物车内商品数量！')
            continue
        if count == SHOPPING_CART[CURRENT_USER][good]['count']:
            SHOPPING_CART[CURRENT_USER].pop(good)
            logger.info('商品 %s x %s 已在购物车删除！' % (good, count))
            if credit_balance > credit_limit:
                credit_balance = credit_limit
                balance += (credit_balance - credit_limit)
        if count < SHOPPING_CART[CURRENT_USER][good]['count']:
            SHOPPING_CART[CURRENT_USER][good]['count'] -= count
            logger.info('商品 %s x %s 已在购物车删除！' % (good, count))
            if credit_balance > credit_limit:
                credit_balance = credit_limit
                balance += (credit_balance - credit_limit)
        credit_balance += (price * count)
        COOKIES[CURRENT_USER]['balance'] = balance
        COOKIES[CURRENT_USER]['credit_balance'] = credit_balance

def order_shoping_cart():
    cost = print_shopping_cart()
    dt = datetime.datetime.now().strftime('%Y%m')
    order_id = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    order_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    params = {
        'mode': 'w',
        'file_path': settings.ORDER_FILE % (name, dt, order_id),
        'data': {
            'order_id': order_id,
            'username': CURRENT_USER,
            'cost': cost,
            'order_time': order_time,
            'goods': SHOPPING_CART[CURRENT_USER]
        }
    }
    confirm = input_string('确认下单？y/n')
    if confirm == 'y':
        utils.file_handler(**params)
        logger.info('用户%s下单成功，请尽快支付！' % CURRENT_USER)
        return True
    logger.info('用户%s取消下单！' % CURRENT_USER)
    return

def pay_shooping_order():
    params = {
        'mode': 'r',
        'file_path': settings.USER_FILE % (CURRENT_USER, CURRENT_USER)
    }
    data = utils.file_handler(**params)
    data['balance'] = COOKIES[CURRENT_USER]['balance']
    data['credit_balance'] = COOKIES[CURRENT_USER]['credit_balance']
    params = {
        'mode': 'w',
        'file_path': settings.USER_FILE % (CURRENT_USER, CURRENT_USER),
        'data': data
    }
    confirm = input_string('确认支付订单？y/n')
    if confirm == 'y':
        if utils.file_handler(**params):
            logger.info('支付成功，请耐心等待发货！')
            SHOPPING_CART[CURRENT_USER] = {}
            return True
    logger.info('用户%s取消支付！' % CURRENT_USER)
    return

def get_shopping_orders(month=None):
    if not month:
        month = datetime.datetime.now().strftime('%Y%m')
    order_dir = settings.ORDER_DIR % (CURRENT_USER, month)
    if utils.checkpath(order_dir):
        file_list = os.listdir(order_dir)
        print('='*50)
        print('%s 订单信息：' % month)
        for f in file_list:
            params = {
                'mode': 'r',
                'file_path': os.path.join(order_dir, f)
            }
            data = utils.file_handler(**params)
            print(data)
        print('=' * 50)

def transfer(account, amount, mode):
    params = {
        'mode': 'r',
        'file_path': settings.USER_FILE % (account, account)
    }
    account_info = utils.file_handler(**params)
    if mode == 'minus':
        if account_info['balance'] < amount:
            logger.warning('账户%s余额不足，转账失败！' % src_account)
            return
        account_info['balance'] -= amount
    elif mode == 'plus':
        account_info['balance'] += amount
    params = {
        'mode': 'w',
        'file_path': settings.USER_FILE % (account, account),
        'data': account_info
    }
    utils.file_handler(**params)
    return True

def transfer_amount():
    src_account = input_string('请输入转账源账户')
    dst_account = input_string('请输入转账目标账户')
    amount = input_number('请输入转账金额')
    for account in [src_account, dst_account]:
        if not settings.USER_FILE % (account, account):
            logger.warning('账户%s不存在！')
            return
    if transfer(src_account, amount, 'minus'):
        transfer(dst_account, amount, 'minus')
        logger.info('账户%s转账%s至账户%s成功！' % (src_account, amount, dst_account))
        return True

def credit_card_bill():
    dt = datetime.date.today().strftime('%Y-%m')
    user_list = os.listdir(USER_DIR)
    for i in user_list:
        if not os.path.isdir(os.path.join(USER_DIR, i)):
            user_list.remove(i)
    for user in user_list:
        params = {
            'mode': 'r',
            'file_path': USER_FILE % (user, user)
        }
        user_info = utils.file_handler(**params)
        if user_info['bill'] == 0:
            user_info['bill'] = (user_info['credit_limit'] - user_info['credit_balance'])
        else:
            user_info['bill'] += (user_info['bill'] * 0.0005)
        params = {
            'mode': 'r',
            'file_path': USER_FILE % (user, user),
            'data': user_info
        }
        utils.file_handler(**params)
        if user_info['bill'] != 0:
            logging.info('用户 %s %s 账单已生成！' % (user, dt))
    return True

def get_credit_card_bill():
    bill = COOKIES[CURRENT_USER]['bill']
    print('='*30)
    print('用户%s每月账单日：22号\n每月还款日：10号\n本期账单: %s' % (CURRENT_USER, bill))
    print('='*30)
    return True

def credit_card_repay():
    params = {
        'mode': 'r',
        'file_path': USER_FILE % (CURRENT_USER, CURRENT_USER)
    }
    user_info = utils.file_handler(**params)
    if user_info['bill'] == 0:
        print('用户%s本期账单是0，不需要还款！' % CURRENT_USER)
        return True
    amount = input_number('请输入还款金额')
    if amount > user_info['bill']:
        user_info['credit_balance'] = user_info['credit_limit']
        user_info['bill'] = 0
        logger.info('用户%s本期账单已还清！' % CURRENT_USER)
    if amount == user_info['bill']:
        user_info['credit_balance'] = user_info['credit_limit']
        user_info['bill'] = 0
        logger.info('用户%s本期账单已还清！' % CURRENT_USER)
    if amount > user_info['bill']:
        user_info['credit_balance'] += amount
        user_info['bill'] -= amount
        logger.info('用户%s本期账单未还清，还需%s还清本期账单！' % (CURRENT_USER, user_info['bill']))
    return True

def credit_card_withdraw_cash():
    global COOKIES
    if COOKIES[CURRENT_USER]['credit_limit'] == 0:
        logger.warning('用户%s信用卡已冻结，无法提现！' % CURRENT_USER)
        return
    amount = input_number('请输入提现金额')
    params = {
        'mode': 'r',
        'file_path': USER_FILE % (CURRENT_USER, CURRENT_USER)
    }
    user_info = utils.file_handler(**params)
    if user_info[CURRENT_USER]['credit_balance'] >= (amount + (amount * 0.05)):
        user_info[CURRENT_USER]['credit_balance'] -= (amount + (amount * 0.05))
    else:
        logger.warning('用户%s信用卡可用额度不足，提现%s失败！' % (CURRENT_USER, amount))
        return
    user_info[CURRENT_USER]['balance'] += amount
    params = {
        'mode': 'r',
        'file_path': USER_FILE % (CURRENT_USER, CURRENT_USER),
        'data': user_info
    }
    utils.file_handler(**params)
    logger.info('用户%s提现%s成功！' % (CURRENT_USER, amount))
    COOKIES[CURRENT_USER]['balance'] = user_info[CURRENT_USER]['balance']
    COOKIES[CURRENT_USER]['credit_balance'] = user_info[CURRENT_USER]['credit_balance']
    return True

def credit_card_manage():
    while True:
        action_menu = {
            '1': ['plus', '提额'],
            '2': ['minus', '降额'],
            '3': ['freeze', '冻结'],
        }
        print('=' * 30)
        for k, v in action_menu.items():
            print('%-6s %-10s' % (k, v[1]))
        print('=' * 30)
        code = input_string('请输入操作编码')
        if code in action_menu:
            operation = action_menu[code][0]
        else:
            logger('操作编码非法！')
            continue
        params = {
            'mode': 'r',
            'file_path': USER_FILE % (CURRENT_USER, CURRENT_USER)
        }
        user_info = utils.file_handler(**params)
        if operation == 'plus':
            amount = input_number('请输入提额金额')
            user_info[CURRENT_USER]['credit_limit'] += amount
            user_info[CURRENT_USER]['credit_balance'] += amount
            logger.info('用户%s信用卡提额完成！' % CURRENT_USER)
        elif operation == 'minus':
            amount = input_number('请输入提额金额')
            user_info[CURRENT_USER]['credit_limit'] -= amount
            user_info[CURRENT_USER]['credit_balance'] -= amount
            logger.info('用户%s信用卡降额完成！' % CURRENT_USER)
        elif operation == 'freeze':
            user_info[CURRENT_USER]['credit_limit'] = 0
            logger.info('用户%s信用卡冻结完成！' % CURRENT_USER)
        params = {
            'mode': 'w',
            'file_path': USER_FILE % (CURRENT_USER, CURRENT_USER),
            'data': user_info
        }
        utils.file_handler(**params)
        return True

def reset_password():
    params = {
        'mode': 'r',
        'file_path': USER_FILE % (CURRENT_USER, CURRENT_USER)
    }
    user_info = utils.file_handler(**params)
    password = input_string(register=True)
    user_info['password'] = password
    params = {
        'mode': 'r',
        'file_path': USER_FILE % (CURRENT_USER, CURRENT_USER),
        'data': user_info
    }
    utils.file_handler(**params)
    logger.info('用户%s重置密码成功！' % CURRENT_USER)
    return True

def lock_user():
    name = input_string('请输入要锁定的用户名', name=True)
    if not utils.checkpath(USER_FILE % (name, name)):
        logger.warning('用户%s不存在！' % name)
        return
    params = {
        'mode': 'r',
        'file_path': USER_FILE % (name, name)
    }
    user_info = utils.file_handler(**params)
    user_info['status'] = 1
    params = {
        'mode': 'r',
        'file_path': USER_FILE % (name, name),
        'data': user_info
    }
    utils.file_handler(**params)
    logger.info('锁定用户%s成功！' % name)
    return True

def remove_user():
    name = input_string('请输入要删除的用户名', name=True)
    if not utils.checkpath(USER_FILE % (name, name)):
        logger.warning('用户%s不存在！' % name)
        return
    params = {
        'mode': 'r',
        'file_path': USER_FILE % (name, name)
    }
    user_info = utils.file_handler(**params)
    if user_info['bill'] > 0:
        logger.warning('用户%s本期账单未还清，无法删除用户！' % name)
        return
    if user_info['credit_balance'] < user_info['credit_limit']:
        logger.warning('用户%s信用卡有未出账账单，无法删除用户！' % name)
        return
    if user_info['balance'] > 0:
        logger.warning('用户%s有账户余额未消费，无法删除用户！' % name)
        return
    os.remove(os.path.join(USER_DIR, name))
    logger.info('删除用户%s完成！' % name)
    return True

def set_permission():
    while True:
        name = input_string('请输入要删除的用户名', name=True)
        if not utils.checkpath(USER_FILE % (name, name)):
            logger.warning('用户%s不存在！' % name)
            return
        params = {
            'mode': 'r',
            'file_path': USER_FILE % (name, name)
        }
        user_info = utils.file_handler(**params)
        action_menu = {
            '1': ['admin', '管理员'],
            '2': ['user', '普通用户'],
        }
        print('=' * 30)
        for k, v in action_menu.items():
            print('%-6s %-10s' % (k, v[1]))
        print('=' * 30)
        code = input_string('请输入操作编码')
        if code in action_menu:
            permission = action_menu[code][0]
        else:
            logger('操作编码非法！')
            continue
        if permission == 'admin':
            user_info['permission'] = 'admin'
        if permission == 'user':
            user_info['permission'] = 'user'
        params = {
            'mode': 'r',
            'file_path': USER_FILE % (name, name),
            'data': user_info
        }
        utils.file_handler(**params)
        logger.info('设置用户%s权限为%s成功！' % (name, permission))
        return True

@auth
def shopping_cart():
    while True:
        shopping_cart_menu = {
            '1': [print_shopping_cart, '查看购物车'],
            '2': [edit_shopping_cart, '编辑购物车'],
            '3': [order_shoping_cart, '下单'],
            '4': [pay_shooping_order, '支付']
        }
        print('=' * 30)
        for k, v in shopping_cart_menu.items():
            print('%-6s %-10s' % (k, v[1]))
        print('=' * 30)
        code = input_string('请输入购物车编码')
        if code in shopping_cart_menu:
            if shopping_cart_menu[code][0]():
                return True
        else:
            logger.info('操作编码非法！')

@auth
def user_manage():
    while True:
        action_menu = {
            '0': [register, '新增用户'],
            '1': [reset_password, '重置密码'],
            '2': [set_permission, '设置权限'],
            '3': [lock_user, '锁定用户'],
            '4': [remove_user, '删除用户'],
            '5': [transfer_amount, '用户转账'],
            '6': [get_credit_card_bill, '获取账单'],
            '7': [credit_card_repay, '还款'],
            '8': [credit_card_withdraw_cash, '提现'],
            '9': [credit_card_manage, '信用卡管理']
        }
        print('=' * 30)
        for k, v in action_menu.items():
            print('%-6s %-10s' % (k, v[1]))
        print('=' * 30)
        code = input_string('请输入用户管理编码')
        if code in action_menu:
            if action_menu[code][0]():
                return True
        else:
            logger.info('操作编码非法！')

def run():
    while True:
        action_menu = {
            '1': [register, '注册'],
            '2': [login, '登录'],
            '3': [shopping, '购物'],
            '4': [shopping_cart, '购物车'],
            '5': [user_manage, 'ATM']
        }
        print('='*30)
        for k,v in action_menu.items():
            print('  %-6s %-10s' % (k, v[1]))
        print('='*30)
        code = input_string('请输入操作编码')
        if code in action_menu:
            try:
                action_menu[code][0]()
            except Exception as e:
                print('\033[33m%s\033[0m' % e)
            except:
                pass
        else:
            logger.info('操作编码非法！')
