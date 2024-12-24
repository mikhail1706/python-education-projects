"""02. Атрибуты класса и функции"""


class Person:
    name = 'Mykhailo'

    def hello(self):
        print('Hello')


print(Person.__dict__)

Person.age = 24

print(Person.__dict__)

print(getattr(Person, 'name'))
setattr(Person, 'dob', '17.06.97')

print(Person.dob)
delattr(Person, 'dob')
print(Person.__dict__)
