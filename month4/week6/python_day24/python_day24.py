# 1. 异常使用
# try:
#     print('start ...')
#     x = 1
#     # y
#     l = []
#     # l[3]
#     d = {'a': 1}
#     # d['b']
#     f = open('a.txt', 'w')
#     f.read()
# except NameError as e:
#     print('NameError: %s' % e)
# except KeyError as e:
#     print('KeyError: %s' % e)
# except IndexError as e:
#     print('IndexError: %s' % e)
# except Exception as e:
#     print('Exception: %s' % e)
# else:
#     print('end ...')
# finally:
#     print('finally ...')
#     f.close()
#     print('file closed ...')
# print('other ...')
#
# 2. 自定义异常
# class RegisterError(BaseException):
#     def __init__(self, msg, user):
#         self. msg = msg
#         self.user = user
#
#     def __str__(self):
#         return '<%s %s>' % (self.user, self.msg)
#
# raise RegisterError('注册失败', 'teacher')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
