"""03. Классы как callable-объекты, экземпляры классов"""


class Person:
    name = 'Mike'

    def hello(self):
        print('Hello')


print(Person.__dict__)

p1 = Person()
p2 = Person()
print(p1)
print(p2)

print(id(p1))
print(id(p2))

print(p1.name)
print(p2.name)

print(id(p1.name))
print(id(p2.name))


print(p1.__dict__)
print(p2.__dict__)

p1.name = 'Oleg'
p2.name = 'Dima'
p2.age = 24

print(p1.__dict__)
print(p2.__dict__)


print(p1.name)
print(p2.name)

new_p1 = Person()
new_p2 = Person()

Person.name = 'My new name'

print(new_p1.name)
print(new_p2.name)


