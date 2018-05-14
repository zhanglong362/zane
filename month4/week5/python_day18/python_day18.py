
# import subprocess
#
# obj = subprocess.Popen('lss -l ~', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#
# res1 = obj.stdout.read()
# print('正确结果: %s' % res1)
#
# res2 = obj.stderr.read()
# print('错误结果1: %s' % res2)
#
# res3 = obj.stderr.read()
# print('错误结果2: %s' % res3)
#
# print(globals())


class OldBoyStudent:
    school = 'OldBoy'

    def learn(self):
        print(' is learning ...')

    def choose(self):
        print('choose course ...')


# print(OldBoyStudent.__dict__['learn'](123))
# print(OldBoyStudent.learn(123))
#
# print(OldBoyStudent.school)

# print(OldBoyStudent.abc)
OldBoyStudent.country = 'China'
OldBoyStudent.school = 'OldBoySchool'

print(OldBoyStudent.__dict__)











