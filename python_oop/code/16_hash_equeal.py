"""16. Хэшируемые объекты и равенство"""


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __hash__(self):
        return hash(self._name)

    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name


p1 = Person('Ivan')
p2 = Person('Ivan')

print(p1 == p2)

p3 = Person('Oleg')

print(p1 == p3)