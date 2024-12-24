"""06. Статические методы и декоратор staticmethod"""


class Person:
    def hello(self):
        print('Hello')

    @staticmethod
    def goodbye():
        print('Goodbye')


a = Person()
b = Person()

a.hello()
a.goodbye()

print(id(a.hello))
print(id(b.hello))

print('---')
print(id(a.goodbye))
print(id(b.goodbye))

print(a.__dict__)
print(b.__dict__)

print(type(a.goodbye))
print(type(a.hello))

Person.goodbye()
