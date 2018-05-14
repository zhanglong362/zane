# -*- encoding: utf-8 -*-

import json
from conf import settings


def read(name):
    with open(r'%s' % settings.USER_CONFIG % name) as f:
        return json.load(f)


def write(user_info):
    with open(r'%s' % settings.USER_CONFIG % user_info['name']) as f:
        json.dump(user_info)

