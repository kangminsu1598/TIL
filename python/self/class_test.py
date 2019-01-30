def create_adder(x):
    def adder(y):
        return x+y
    return adder

a = create_adder(15)
print(a(10))


class Person:
    pop = 0
    def __init__(self):
        self.pop = 10
        Person.pop += 1
    @classmethod
    def showpop(cls):
        print(cls.pop)
    @staticmethod
    def adder(x, y):
        return x+y
p1 = Person()
p2 = Person()
p1.showpop()
del Person
print(p1.adder(5, 8))