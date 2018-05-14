#coding:utf-8
import os,json
from conf import settings

def select(name):
    path = r'%s\%s.json' %(settings.DB_PATH,name)
    if os.path.isfile(path):

        with open(path,'r',encoding='utf-8') as f:
            return json.load(f)
    else:
        return False


def update(user_dic):
    path = r'%s\%s.json' % (settings.DB_PATH, user_dic['name'])
    with open(path,'w',encoding='utf-8') as w:
        json.dump(user_dic,w)

