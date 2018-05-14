# -*- encoding: utf-8 -*-

import os
import pickle
from conf import settings


def save(obj):
    path_obj = os.path.join(settings.BASE_DB, obj.__class__.__name__.lower())
    if not os.path.exists(path_obj):
        os.mkdir(path_obj)
    path_file = os.path.join(path_obj, obj.name)
    with open(r'%s' % path_file, 'wb') as f:
        pickle.load(obj, f)
        f.flush()

def select(name, obj_type):
    path_obj = os.path.join(settings.BASE_DB, obj_type)
    if not os.path.exists(path_obj):
        os.mkdir(path_obj)
    path_file = os.path.join(path_obj, name)
    if not os.path.exists(path_file):
        return
    with open(path_file, 'rb') as f:
        return pickle.load(f)


