# -*- encoding: utf-8 -*-

import os
import json
from conf import settings

def read(name):
    path = os.path.join(settings.BASE_DB, '%s.json' % name)
    if not os.path.exists(path) or os.path.isdir(path):
        return
    with open(r'%s' % path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write(dic):
    path = os.path.join(settings.BASE_DB, '%s.json' % dic['name'])
    with open(r'%s' % path, 'w', encoding='utf-8') as f:
        json.dump(dic, f)
    if os.path.exists(path):
        return True
