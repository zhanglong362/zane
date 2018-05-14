#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from core import app








if __name__ == '__main__':
    app.run()
