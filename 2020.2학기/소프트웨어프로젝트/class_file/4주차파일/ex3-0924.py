class Parent:
    house = "yong-san"
    def __init__(self):
        self.money = 10000

class Child1(Parent):
    def __init__(self):
        super().__init__()
        pass

class Child2(Parent):
    def __init__(self):
        pass

child1 = Child1()
child2 = Child2() # Child2에서는 부모 class의 __init__ 값(생성자)을 불러오지 않았기 때문에 money 변수가 없다. 

print('Child1', dir(child1))
print('Child2', dir(child2))

class A():
    pass
a = A()
print("A",dir(a))
for attr in a.__dir__():
    print(attr)