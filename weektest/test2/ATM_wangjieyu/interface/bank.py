from db import db_hander
from lib import common
from interface import user

logger_bank = common.get_logger('Bnak')


def get_bank_interface(name):
    return user.select_t(name)['account']

def transfer_interface(from_name, to_name, account):
    from_user_dic = user.select_t(from_name)
    to_user_dic = user.select_t(to_name)
    if from_user_dic['account']>=account:
        from_user_dic['account'] -= account
        to_user_dic['account'] += account
        from_user_dic['liushui'].extend(['%s transfer %s yuan to %s' % (from_name, account, to_name)])
        to_user_dic['liushui'].extend(['%s accept %s yuan from %s' % (to_name, account, from_name)])
        db_hander.update(from_user_dic)
        db_hander.update(to_user_dic)
        logger_bank.info('%s 向 %s 转账 %s' % (from_name, to_name, account))
        return True
    else:
        return False



def check_record(name):
    current_user = user.select_t(name)
    logger_bank.info('%s 查看了银行流水' % name)
    return current_user['liushui']

