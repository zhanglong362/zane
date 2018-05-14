# -*- encoding: utf-8 -*-

import os
import pickle
from conf import settings
from lib import common

logger = common.get_logger('db_handler')

def select(name):
    obj_path = os.path.join(settings.DB_PATH, name)
    if not os.path.exists(obj_path):
        return
    if os.path.isdir(obj_path):
        return
    with open(r'%s' % obj_path, 'rb') as f:
        return pickle.load(f)

def update(obj):
    obj_path = os.path.join(settings.DB_PATH, obj.name)
    try:
        with open(r'%s' % obj_path, 'wb') as f:
            pickle.dump(obj, f)
            f.flush()
    except Exception as e:
        logger.warning('写文件出错：%s' % e)
        return
    else:
        return True









