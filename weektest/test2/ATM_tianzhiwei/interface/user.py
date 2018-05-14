from db import db_hand
from lib import common
logger_user=common.logger('User')
def get_info(name):
    return db_hand.select(name)
def write_info(name,password,account=15000):
    dic={'name':name,'password':password,'account':account,'position':account,'state1':False,'write_log':[]}
    db_hand.add(name,dic)
    logger_user.info('%s注册成功'%name)
def write_state(name):
    dic=db_hand.select(name)
    dic['state1']=True
    db_hand.add(name,dic)
