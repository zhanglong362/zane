# -*- encoding: utf-8 -*-

import os
import pickle
from conf import settings

def select(name, obj_type):
    obj_path = os.path.join(settings.DB_PATH, obj_type)
    if not os.path.exists(obj_path):
        os.mkdir(obj_path)
    file_path = os.path.join(obj_path, name)
    if not os.path.exists(file_path):
        return
    with open(r'%s' % file_path, 'rb') as f:
        return pickle.load(f)

def save(obj):
    obj_path = os.path.join(settings.DB_PATH, obj.__class__.__name__.lower())
    if not os.path.exists(obj_path):
        os.mkdir(obj_path)
    file_path = os.path.join(obj_path, obj.name)
    with open(r'%s' % file_path, 'wb') as f:
        pickle.dump(obj, f)
        f.flush()
    if os.path.exists(file_path):
        return True

