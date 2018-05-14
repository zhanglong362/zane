# -*- encoding: utf-8 -*-

from db import modules

def login(name, password):
    obj = modules.Admin.get_obj_by_name(name)
    if obj:
        if obj.name == name and obj.password == password:
            return True, '用户%s登陆成功！' % name
        else:
            return False, '用户名或密码错误！'
    else:
        return False, '用户%s未注册！' % name

def register(name, password):
    obj = modules.Admin.get_obj_by_name(name)
    if obj:
        return False, '用户%s已注册！' % name
    else:
        modules.Admin(name, password)
        return True, '用户%s注册成功！' % name







