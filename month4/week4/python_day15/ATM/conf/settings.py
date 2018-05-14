# -*- encoding: utf-8 -*-
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_FILE = '%s/db/db.txt' % BASE_DIR

LOG_FILE = '%s/logs/access.log' % BASE_DIR