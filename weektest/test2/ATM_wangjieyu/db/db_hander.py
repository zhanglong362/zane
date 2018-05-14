import os,json

BASE_DB=os.path.dirname(os.path.dirname(__file__))

def select(name):
    BASE_USER = os.path.join(BASE_DB,'db','%s.json' %name)
    if os.path.exists(BASE_USER):
        with open(BASE_USER,'r',encoding='utf-8') as f:
            user_dic=json.load(f)
        return user_dic
    else:
        return False

def update(user_dic):
    BASE_USER = os.path.join(BASE_DB,'db','%s.json' %user_dic['name'])
    with open(BASE_USER,'w',encoding='utf-8') as f:
        json.dump(user_dic,f)

