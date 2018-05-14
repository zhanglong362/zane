#
# class OldboyStudent():
#     n = 0
#
#     def __init__(self):
#         OldboyStudent.n += 1
#
# stu1 = OldboyStudent()
# print(OldboyStudent.n)
# stu2 = OldboyStudent()
# print(OldboyStudent.n)
# stu3 = OldboyStudent()
# print(OldboyStudent.n)
#
# # print(stu1.n)
# # print(stu2.n)
# # print(stu3.n)

class Human:
    def __init__(self, name, human_species, attack, health_point=100):
        self.name = name
        self.human_species = human_species
        self.attack = attack
        self.health_point = health_point

    def bite(self, enemy):
        enemy.health_point -= self.attack
        print('''
        %s => %s 咬了 %s => %s
        %s 掉血 %s
        %s 生命值 %s
        ''' % (self.human_species,
               self.name,
               enemy.dog_breeds,
               enemy.name,
               enemy.dog_breeds,
               self.attack,
               enemy.dog_breeds,
               enemy.health_point))

class Dog:
    def __init__(self, name, dog_breeds, attack, health_point=100):
        self.name = name
        self.dog_breeds = dog_breeds
        self.attack = attack
        self.health_point = health_point

    def bite(self, enemy):
        enemy.health_point -= self.attack
        print('''
        %s => %s 咬了 %s => %s
        %s 掉血 %s
        %s 生命值 %s
        ''' % (self.dog_breeds,
               self.name,
               enemy.human_species,
               enemy.name,
               enemy.human_species,
               self.attack,
               enemy.human_species,
               enemy.health_point))

p = Human('袁誓隆', '黑人', 200)
d = Dog('吴晨钰', '小奶狗', 5)
p.bite(d)
d.bite(p)




