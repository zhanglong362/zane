# -*- encoding: utf-8 -*-

import os
import pickle
from conf import settings

def save(obj):
    obj_path = os.path.join(settings.BASE_DB, obj.__class__.__name__)
    if not os.path.exists(obj_path):
        os.mkdir(obj_path)
    file_path = os.path.join(obj_path, obj.name)
    with open(r'%s' % file_path, 'wb') as f:
        pickle.dump(obj, f)

def select(name, obj_type):
    obj_path = os.path.join(settings.BASE_DB, obj_type.lower())
    if not os.path.exists(obj_path):
        os.mkdir(obj_path)
    file_path = os.path.join(obj_path, name)
    if not os.path.exists(file_path):
        return
    with open(r'%s' % file_path, 'rb') as f:
        return pickle.load(f)



