from db import db_hander

def select_t(name):
    return db_hander.select(name)

def update_t(name,passwd,account=15000):
    user_dic = {'name': name, 'passwd': passwd, 'locked': False, 'account': account, 'liushui':[]}
    db_hander.update(user_dic)
    # logger_user.info('%s 注册了' % name)