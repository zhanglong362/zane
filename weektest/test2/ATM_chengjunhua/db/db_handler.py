import os
import json
from conf import settings

# 查
def find_file(name):
    if  os.path.exists(settings.BASE_DB % name) :
        with open(settings.BASE_DB % name, 'r', encoding='utf-8') as f:
            user_dic = json.load(f)
            return user_dic
    return False


# 增改
def update(user_dic):
    with open(settings.BASE_DB%user_dic['name'],'w',encoding='utf-8') as f:
        json.dump(user_dic,f)





