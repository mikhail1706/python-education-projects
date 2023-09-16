"""15. Полиморфизм, перегрузка операторов
   Полиморфизм - разное поведение одного и того же метода для разных классов
"""


class Room:
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.area = self.x * self.y

    def __add__(self, other):
        if isinstance(other, Room):
            return self.area + other.area

        raise TypeError('Wrong object')

    def __eq__(self, other):
        if isinstance(other, Room):
            return self.area == other.area


r1 = Room(3, 5)
r2 = Room(4, 7)

print(r1.area)
print(r2.area)

print('Add: ', r1 + r2)
print('Equal: ', r1 == r2)