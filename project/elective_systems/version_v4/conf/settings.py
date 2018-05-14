# -*- encoding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'db')
ACCESS_LOG = os.path.join(BASE_DIR, 'logs', 'access.log')

# 日志输出格式
STANDARD_FMT = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                '[%(levelname)s][%(message)s]'
SIMPLE_FMT = '%(asctime)s %(message)s'

# logging 配置字典
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        # 标准日志格式
        'standard_fmt': {
            'format': STANDARD_FMT
        },
        # 简单日志格式
        'simple_fmt': {
            'format': SIMPLE_FMT
        },
    },
    'filters': {},
    'handlers': {
        # 文件日志
        'default': {
            'level': 'DEBUG',
            # 日志输出到文件，且基于文件大小切分
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard_fmt',
            'filename': ACCESS_LOG,
            # 每个日志文件大小 1Gb
            'maxBytes': 1024*1024*1024,
            # 保留日志文件数
            'backupCount': 5,
            # 日志文件编码 utf-8
            'encoding': 'utf-8',
        },
        # 屏幕日志
        'console': {
            'level': 'DEBUG',
            # 日志输出到流
            'class': 'logging.StreamHandler',
            'formatter': 'simple_fmt'
        },
    },
    'loggers': {
        # logger对象配置
        '': {
            # 配置日志handlers
            'handlers': ['default'],
            'level': 'DEBUG',
            # 启用日志继承
            'propagate': True,
        },
    },
}



