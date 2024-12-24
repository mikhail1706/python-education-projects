"""13. Наследование, перегрузка методов и расширение функциональности"""


class IntelCpu:
    cpu_socket = 1151
    name = 'Intel'


class I7(IntelCpu):
    pass


class I5(IntelCpu):
    pass


i5 = I5()
i7 = I7()

print(isinstance(i5, IntelCpu))

print(type(i5))


class One:
    pass


class Two(One):
    pass


class Three(Two):
    pass


print(issubclass(Three, One))
print(isinstance(i5, type(i7)))


class Person:
    def hello(self):
        print('I am Person')


class Student(Person):
    # def hello(self):
    #     print('I am Student')

    def goodbye(self):
        print('Goodbye')


s = Student()

s.hello()


class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f'Hello from {self.name}')


class Student(Person):
    pass


s = Student('John')
s.hello()
