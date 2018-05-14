from interface import user
from interface import bank
from lib import common

panduan={
    'name':None,
    'is_auth':False
}
logger_bank = common.get_logger('Bnak')

def register():
    while True:
        name = input('输入你的账号: ').strip()
        if not name.isalnum():continue
        user_dic=user.select_t(name)
        if user_dic:
            print('账户已存在 ggg')
            continue
        else:
            passwd=input('输入你的账户密码').strip()
            passwd1=input('确认你输入的账户密码').strip()
            if passwd==passwd1:
                user.update_t(name,passwd)
                print('注册成功')
                break
            else:
                print('密码不一致')

def login():
    while True:
        name = input('输入你的账号: ').strip()
        if not name.isalnum():continue
        user_dic=user.select_t(name)
        # print(user_dic)
        if user_dic:
            passwd=input('输入你的账户密码').strip()
            if passwd==user_dic['passwd']:
                panduan['name']=name
                panduan['is_auth']=True
                print('登陆成功')
                break
            else:
                print('密码错误')
                continue
        else:
            print('账户不存在 ggg')
            break

@common.login_auth
def chaxun():
    balance = bank.get_bank_interface(panduan['name'])
    print('查看余额')
    print('您的余额为：%s' % balance)

@common.login_auth
def qukuan():
    while True:
        user_dic=user.select_t(panduan['name'])
        money=input('取多少 速度。。。').strip()
        if not money.isdigit():continue
        money=int(money)
        user_dic['account']-=money
        user.update_t(user_dic['name'],user_dic['passwd'],user_dic['account'])
        print('您取走了%s $,还剩%s $' %(money,user_dic['account']))
        logger_bank.info('%s 取款 %s 元' % (user_dic['name'], user_dic['account']))
        break

@common.login_auth
def huankuan():
    while True:
        user_dic=user.select_t(panduan['name'])
        money=input('还多少 速度。。。').strip()
        if not money.isdigit():continue
        money=int(money)
        user_dic['account']+=money
        user.update_t(user_dic['name'],user_dic['passwd'],user_dic['account'])
        print('您还了%s $,还剩%s $' %(money,user_dic['account']))
        logger_bank.info('%s 还款 %s 元' % (user_dic['name'], user_dic['account']))
        break

@common.login_auth
def liushui_():
    print('您的银行流水为：')
    for record in bank.check_record(panduan['name']):
        print(record)

@common.login_auth
def zhuanzhang():
    print('转账')
    while True:
        trans_name = input('输入你的转账用户(q to exit)>>').strip()
        if trans_name == panduan['name']:
            print('不能是本人')
            continue
        if 'q' == trans_name: break
        trans_dic = user.select_t(trans_name)
        if trans_dic:
            trans_money = input('输入转账金额 >>:').strip()
            if trans_money.isdigit():
                trans_money = int(trans_money)
                user_balance = bank.get_bank_interface(panduan['name'])
                if user_balance >= trans_money:
                    bank.transfer_interface(panduan['name'], trans_name, trans_money)
                    break
                else:
                    print('钱不够')
                    continue
            else:
                print('输入数字')
                continue
        else:
            print('账户不存在')
            continue
fun_dic={
    '1':register,
    '2':login,
    '3':chaxun,
    '4':qukuan,
    '5':huankuan,
    '6':zhuanzhang,
    '7':liushui_,
}

def run():
    while True:
        choice=input('''
        1、注册
        2、登陆
        3、查询
        4、取款
        5、还款
        6、转账
        7、流水
>>>>>>>>>>>>>   ''').strip()
        if choice not in fun_dic:continue
        fun_dic[choice]()

