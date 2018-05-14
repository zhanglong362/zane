# 修改余额
from db import db_handler
def update_money(user_dic):
    db_handler.update(user_dic)


