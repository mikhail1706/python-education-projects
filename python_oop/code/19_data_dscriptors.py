"""19. Дескрипторы данных"""

from time import time
import ctypes

# class Epoch:
#     def __get__(self, instance, owner):
#         print(f'id of self: {id(self)}')
#         if instance is None:
#             return self
#         return int(time())
#
#     def __set__(self, instance, value):
#         pass
#
#
# class MyTime:
#     epoch = Epoch()
#
#
# m = MyTime()
# m1 = MyTime()
# print(m.epoch)
# print(m1.epoch)
# print(MyTime.epoch)


def ref_count(obj_id):
    return ctypes.c_long.from_address(obj_id).value


class IntegerDescriptor:

    def __init__(self):
        self._values = {}

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




