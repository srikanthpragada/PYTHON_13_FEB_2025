class Person:
    def __init__(self, name, age):
        self.name = name   # public
        self.__age = age   # private

    def show(self):
        print(self.name, self.__age)


p1 = Person("Bill", 70)
p1.show()
print(p1.__dict__)

print(p1.name, p1._Person__age)
