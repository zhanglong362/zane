# -*- encoding: utf-8 -*-

import os
import json
import logging
from conf import settings

def get_logger(name=__name__):
    '''
    For get a logger object.
    :param name: logger object name
    :return: logger object
    '''
    logging.config.dictConfig(settings.LOGGING_CONFIG)
    logger = logging.getLogger(name)
    return logger

logger = get_logger('utils')

def checkpath(uri):
    '''
    Check File or Directory exists
    :param uri: file uri
    :return: True or False
    '''
    return os.path.exists(uri)

def file_handler(**kwargs):
    '''
    File handler to read json data to file or write json data from file.
    :param
        kwargs: **{'name': name, 'uri': file_uri, 'data': write_data}
    :return:
        read: read success return json data
        write: write success return True
    '''
    dir_path = os.path.dirname(kwargs['file_path'])
    file_path = kwargs['file_path']
    mode = kwargs['mode']
    try:
        if not checkpath(dir_path):
            os.makedirs(dir_path)
    except:
        logger.error('mkdir %s error' % dir_path)
        return
    if mode == 'r':
        try:
            with open(r'%s' % file_path, 'r') as f:
                data = json.load(f)
                return data
        except:
            logger.error('read %s error' % file_path)
            return
    elif mode == 'w':
        try:
            with open(r'%s' % file_path, 'w') as f:
                json.dump(kwargs['data'], f)
                return True
        except:
            logger.error('write %s error' % file_path)
            return
    else:
        logger.error('"%s"不是正确的文件打开模式！' % mode)





