"""17. super() и делегирование родителям"""


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# class Student(Person):
#     def __init__(self, name, surname):
#         super().__init__(name)
#         self.surname = surname
#
#
# s = Student('Mike', 'Humen')
# print(s.__dict__)


class Person:
    def hello(self):
        print(f'Bound with {self}')


class Student(Person):
    def hello(self):
        print('Student obj.hello() is called')
        super().hello()


s = Student()
s.hello()
print(hex(id(s)))
