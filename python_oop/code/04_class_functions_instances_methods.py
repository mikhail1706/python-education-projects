"""04. Функции классов и методы экземпляров"""


class Person:
    def hello(self):
        print('hello')


print(Person.hello)

p = Person()

print(p.hello)

# convert 16
print(hex(id(p)))

Person.hello(p)
# p.hello()

print(type(p.hello))            # method
print(type(Person.hello))       # function --> to instance method

print(p.__dict__)
print(p.hello.__func__)

# p.hello.__func__(hello.__self__, *args)
