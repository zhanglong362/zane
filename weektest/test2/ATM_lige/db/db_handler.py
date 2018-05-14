import os
from conf import setting
import json
def update(user_dic):
    '''
    把传入的用户字典序列化到json文件中
    :param user_dic:
    :return:
    '''
    path_file=os.path.join(setting.BASE_DIR,'db','%s.json' %user_dic['name'])
    with open(path_file, 'w', encoding='utf-8') as f:
        json.dump(user_dic, f)
        f.flush()


def select(name):
    '''
    通过名字查询到本人的字典信息，当人不存在的时候，返回False
    :param name:
    :return:
    '''
    path_file = os.path.join(setting.BASE_DIR, 'db', '%s.json' % name)
    if os.path.exists(path_file):
        with open(path_file,'r',encoding='utf-8')as f:
            return json.load(f)

    else:
        return False