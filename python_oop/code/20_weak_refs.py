"""20. Слабые ссылки weakref и проблема хранения
       данных в экземпляре дескриптора
"""

# import weakref
# from pprint import pprint
#
#
# class Person:
#     pass
#
#
# p = Person()
# w = weakref.ref(p)

# check ref state
# print(w)
# print(hex(id(p)))
# del p
# print(w)

# deal ref if Object is dead
# print(w())
# del p
# print(w())


# d = weakref.WeakKeyDictionary()
# print(d)
#
# d[p] = 10
# print(d[p])
# pprint(dir(d))
# print(d.keyrefs())
# del p
# print(d.keyrefs())

from weakref import WeakKeyDictionary


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __eq__(self, other):
#         return isinstance(other, Person) and self.name == other.name
#
#     def __hash__(self):
#         return hash(self.name)

class IntegerDescriptor:

    def __init__(self):
        self._values = WeakKeyDictionary()

    def __set__(self, instance, value):
        self._values[instance] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance, None)


class Vector:
    x = IntegerDescriptor()
    y = IntegerDescriptor()


v1 = Vector()
v2 = Vector()



