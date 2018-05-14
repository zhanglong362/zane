# encoding: utf-8

import hmac
import logging.config
from conf import settings

class Common:
    @classmethod
    def get_logger(cls, name=__name__):
        logging.config.dictConfig(settings.LOGGING_CONFIG)
        return logging.getLogger(name)

    @classmethod
    def make_hmac_code(cls, msg):
        h = hmac.new(b'ElectiveSystems')
        h.update(msg)
        return h.hexdigest()

