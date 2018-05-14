# -*- encoding: utf-8 -*-

from conf import settings
print(settings.LOG_FILE)

def logger(msg):
    print('日志 ...')
    with open(settings.LOG_FILE, 'a') as f:
        f.write('%s\n' % msg)
