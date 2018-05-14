# -*- encoding: utf-8 -*-

import os
import json
from conf import settings

def read(name):
    if os.path.exists(settings.USER_FILE % name):
        with open(r'%s' % settings.USER_FILE % name) as f:
            return json.load(f)

def write(user_dic):
    with open(r'%s' % settings.USER_FILE % user_dic['name'], 'w') as f:
        json.dump(user_dic, f)
        return True

