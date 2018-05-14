import os
import json
from conf import setting

def update(user_dic):
    path_file=os.path.join(setting.BASE_DIR,'db','%s.json' %user_dic['name'])
    with open(path_file,'w',encoding='utf-8')as f:
        json.dump(user_dic,f)
        f.flush()


def  select(name):
    path_file = os.path.join(setting.BASE_DIR, 'db', '%s.json' %name)
    if os.path.exists(path_file):
        with open(path_file,'r',encoding='utf-8')as f:
           return json.load(f)
    else:
        return False