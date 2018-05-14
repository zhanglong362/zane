# -*- encoding: utf-8 -*-

import pickle
from conf import settings

class Db:
    @classmethod
    def read(cls):
        with open(r'%s' % settings.DATA_FILE, 'rb') as f:
            return pickle.load(f)
    @classmethod
    def write(cls, data):
        with open(r'%s' % settings.DATA_FILE, 'wb') as f:
            pickle.dump(data, f)
