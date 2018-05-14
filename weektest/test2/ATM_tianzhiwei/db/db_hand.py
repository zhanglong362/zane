import os
import json
from conf import settings
def select(name):
    path=r'%s\%s.json'%(settings.DBSE_PATH,name)
    if os.path.exists(path):
        with open(path,'r',encoding='utf8')as f:
            return json.load(f)
    else:
        return False
def add(name,dic):
    path = r'%s\%s.json' % (settings.DBSE_PATH, name)
    with open(path, 'w', encoding='utf8')as f:
         json.dump(dic,f)