# 4月9日作业：
# == == 必做作业 == ==
# 用谷歌浏览器打开http: // maoyan.com /，点击榜单，然后点击鼠标右键选择：显示网页源代码，然后将显示出的内容存储到文件index.html中
# 1、匹配出文件index.html所有的链接
import re

with open(r'index.html') as f:
    data = f.read()
hyperlinks = re.findall('href="(http.*?)"', data)
print(hyperlinks)

# 2、有字符串
# 'email1:378533872@qq.com email2:333312312@163.com eamil3:alexsb123@gmail.com'
# 匹配出所有的邮箱地址：['378533872@qq.com', '333312312@163.com', 'alexsb123@gmail.com']
import re

s = 'email1:378533872@qq.com email2:333312312@163.com eamil3:alexsb123@gmail.com'
mailboxes = re.findall(':(.*?.com)', s)
print(mailboxes)

# 3、编写程序，
# 1、让用户输入用户名，要求用户输入的用户名只能是字母或数字，否则让用户重新输入，
# 2、让用户输入密码，要求密码的长度为8 - 10位，
# 密码的组成必须为字母、数字、下划线，密码开头必须为字母，否则让用户重新输入
import re

def name_convention():
    while True:
        name = input('请输入用户名 >>: ').strip()
        if re.findall('[^0-9a-zA-Z]', name):
            print('用户名必须是字母或数字！')
            continue
        return name

def password_convention():
    while True:
        password = input('请输入密码 >>: ')
        if len(password) not in (8, 9, 10):
            print('密码长度必须是 8-10 位！')
            continue
        if re.findall('^[^a-zA-Z]', password):
            print('密码必须以字母开头！')
            continue
        if re.findall('\W', password):
            print('密码必须为字母、数字、下划线！')
            continue
        return password

def register():
    name = name_convention()
    password = password_convention()
    user_info = {
        'name': name,
        'password': password
    }
    print('用户%s注册成功！' % name)

register()

# 4、有字符串
# "1-12*(60+(-40.35/5)-(-4*3))"，匹配出所有的数字如['1', '-12', '60', '-40.35', '5', '-4', '3']
s = "1-12*(60+(-40.35/5)-(-4*3))"
numbers = re.findall('-?\d+[.]\d+|-?\d+', s)
print(numbers)
# 5、有字符串
# "1-2*(60+(-40.35/5)-(-4*3))"，找出所有的整数如['1', '-2', '60', '', '5', '-4', '3']
s = "1-2*(60+(-40.35/5)-(-4*3))"
numbers = re.findall("-?\d+\.\d*|(-?\d+)", s)
print(numbers)
# 6、ATM + 购物车作业：
# 1、构建程序基本框架
# 2、实现注册功能

# 7、明天早晨默写6
#
# == == 答案 == ==
# 答案：
# 1、re.findall('href="(.*?)"', 读取文件内容)
# 2、re.findall(r":(.*?@.*?com)", 'email1:378533872@qq.com email2:333312312@163.com eamil3:alexsb123@gmail.com')
# 3、
# 1、判断用户输入的内容中如果匹配到[ ^ a - zA - Z0 - 9]则让用户重新输入
# 2、 ^ [a - zA - Z]\w
# {7, 10}$
#
#
# 4、re.findall(r'-?\d+\.?\d*', "1-12*(60+(-40.35/5)-(-4*3))")
# 5、re.findall(r"-?\d+\.\d*|(-?\d+)", "1-2*(60+(-40.35/5)-(-4*3))")
#
# 6、略
#
# 7、略
#
#  == 可以考虑选做一个作业（不做完全可以）：正则表达式 + 函数递归调用实现一个计算器 ==
# 用户输入：1 - 2 * ((60 + 2 * (-3 - 40.0 / 5) * (9 - 2 * 5 / 3 + 7 / 3 * 99 / 4 * 2998 + 10 * 568 / 14)) - (-4 * 3) / (
#             16 - 3 * 2))
# 可以得到计算的结果
#
# 参考：http://www.cnblogs.com/wupeiqi/articles/4949995.html