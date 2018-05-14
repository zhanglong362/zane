# -*- encoding: utf-8 -*-

class Meta(Foo):
    pass

class Foo:
    pass

class Bar(Foo):
    pass

l = [Foo.__bases__,
     Foo.__class__,
     Foo.__name__,
     Foo.__mro__,
     Bar.__bases__,
     Bar.__class__]

for i in l:
    print(i)





