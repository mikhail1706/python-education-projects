"""18. Дескрипторы. Non-data дескрипторы"""


# class Person:
#     def __init__(self, name, surname):
#         self._surname = surname
#         self._name = name
#         self._full_name = None
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         self._name = value
#         self._full_name = None
#
#     @property
#     def surname(self):
#         return self._surname
#
#     @surname.setter
#     def surname(self, value):
#         self._surname = value
#         self._full_name = None


# class StringD:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self._value = value
#
#     def get(self):
#         return self._value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = StringD(name)
#         self.surname = StringD(surname)


# p = Person('Mykhailo', 'Humen')


from time import time
from random import choice


class Epoch:
    def __get__(self, instance, owner):
        return int(time())


class MyTime:
    epoch = Epoch()


# m = MyTime()
# print(m.epoch)


class Dice:
    @property
    def number(self):
        return choice(range(1, 7))


class Choice:
    def __init__(self, *choice):
        self._choice = choice

    def __get__(self, instance, owner):
        return choice(self._choice)


class Game:
    dice = Choice(1, 2, 3, 4, 5, 6)
    flip = Choice('Heads', 'Tails')
    rock_paper_scissors = Choice('rock', 'paper', 'scissors')


# class Game:
#     @property
#     def rock_paper_scissors(self):
#         return choice(['Rock', 'Paper', 'Scissors'])
#
#     @property
#     def flip(self):
#         return choice(['Heads', 'Tails'])
#
#     @property
#     def dice(self):
#         return choice(range(1, 7))


g = Game()
print(g.dice)

