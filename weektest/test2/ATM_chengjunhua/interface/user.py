import os
from db import db_handler


#查
def file(name):
    user_dic=db_handler.find_file(name)
    if user_dic:
        return user_dic
    return False


#增改
def update_user(name,password,balance=15000,account=15000,lock=False):
    user_dic={'name':name,'password':password,'balance':balance,'account':account
              ,'lock':lock}
    db_handler.update(user_dic)



#锁定用户
def lock_user_interface(name):
    user_dic=db_handler.find_file(name)
    user_dic['lock'] = True
    db_handler.update(user_dic)