# -*- encoding: utf-8 -*-

import json
from lib import common
from conf import settings

logger = common.get_logger('db_handler')

def file_handler_read(name):
    try:
        with open(r'%s' % settings.USER_FILE % name) as f:
            data = json.load(f)
    except Exception as e:
        logger.warning('读取文件失败：%s' % e)
    else:
        return data

def file_handler_write(user_info):
    try:
        with open(r'%s' % settings.USER_FILE % user_info['name'], 'w') as f:
            json.dump(user_info, f)
    except Exception as e:
        logger.warning('写入文件失败：%s' % e)
    else:
        return True




