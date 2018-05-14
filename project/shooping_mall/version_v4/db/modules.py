# -*- encoding: utf-8 -*-

from db import db_handler

class Base:
    @staticmethod
    def get_obj_by_name(name):
        return db_handler.select(name)

    def save(self):
        return db_handler.update(self)


class User(Base):
    def __init__(self, name, password, credit_limit):
        self.name = name
        self.password = password
        self.balance = 0
        self.bill = 0
        self.flow = []
        self.credit_balance = credit_limit
        self.credit_limit = credit_limit

    @classmethod
    def register(cls, name, password, credit_limit):
        user = cls(name, password, credit_limit)
        return user.save()

    def check_balance(self):
        info = '''
        账户余额：%s
        信用卡余额：%s
        信用卡额度：%s
        ''' % (self.balance, self.credit_balance, self.credit_limit)
        return info

    def check_bill(self):
        bill = '本期账单为%s元！' % self.bill
        return bill

    def check_flow(self, bill_date):
        flow = []
        for f in self.flow:
            if bill_date in f[0]:
                flow.append(f)
        return flow


