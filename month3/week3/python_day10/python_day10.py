#
# config = r'db.txt'
#
# def get_uname():
#     while True:
#         uname = input('name >>: ').strip()
#         if not uname.isalpha():
#             continue
#         with open(config, 'r', encoding='utf-8') as f:
#             for line in f:
#                 uinfo = line.strip('\n').split(',')
#                 if uname == uinfo[0]:
#                     print('\033[31m用户已存在...\033[0m')
#                     break
#             else:
#                 return uname
#
# # print(get_uname())
#
# help(get_uname)


#
# def auth():
#     print('登陆...')
#
# def register():
#     print('注册...')
#
# def search():
#     print('查看...')
#
# def transfer():
#     print('转账...')
#
# def pay():
#     print('支付...')
#
# dic = {
#     '1': auth,
#     '2': register,
#     '3': search,
#     '4': transfer,
#     '5': pay
# }
#
# def interactive():
#     while True:
#         print('''
#         1  登陆
#         2  注册
#         3  查看
#         4  转账
#         5  支付
#         ''')
#         choice = input('>>: ').strip()
#         if choice in dic:
#             dic[coice]()
#         else:
#             print('非法操作！')


def outter():
    x = 2
    def inner():
        # x = 1
        print('from inner %s' % x)
    return inner

f = outter()         # f = inner
print(f)
x = 11111111111
f()

def foo():
    x = 111111111111
    f()

foo()


