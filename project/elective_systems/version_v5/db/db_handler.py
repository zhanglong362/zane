#-*- encoding: utf-8 -*-

import os
import pickle
from conf import settings

def select(name, type_name):
    type_path = os.path.join(settings.BASE_DB, type_name)
    if not os.path.exists(type_path):
        os.mkdir(type_path)
    obj_path = os.path.join(type_path, name)
    if not os.path.exists(obj_path):
        return
    with open(r'%s' % obj_path, 'rb') as f:
        return pickle.load(f)

def save(obj):
    type_path = os.path.join(settings.BASE_DB, obj.__class__.__name__.lower())
    if not os.path.exists(type_path):
        os.mkdir(type_path)
    obj_path = os.path.join(type_path, obj.name)
    with open(r'%s' % obj_path, 'wb') as f:
        pickle.dump(obj, f)
        f.flush()
        return True
