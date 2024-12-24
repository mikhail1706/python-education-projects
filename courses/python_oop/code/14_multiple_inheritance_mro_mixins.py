"""14. Множественное наследование, MRO, миксины"""


class FoodMixin:
    food = None

    def get_food(self):
        if self.food is None:
            raise ValueError('Food should be set')
        print(f'I like {self.food}')


class Person:
    def hello(self):
        print('I am Person')


class Student(FoodMixin, Person):
    food = 'Pizza'

    def hello(self):
        print('I am Student')


class Prof(Person):
    def hello(self):
        print('I am Prof')


class Someone(Prof, Student):
    pass


someone = Someone()

s = Student()

s.hello()
print(s.__class__.mro())

someone.get_food()
