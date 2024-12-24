"""12. Свойства только для чтения и вычисляемые свойства"""


class Person:
    def __init__(self, name, surname):
        self._surname = surname
        self._name = name
        self._full_name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._full_name = None

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value
        self._full_name = None

    @property
    def full_name(self):
        if self._full_name is None:
            self._full_name = f'{self._name} {self._surname}'

        return self._full_name


p = Person('Mykhailo', 'Humen')

print(p.__dict__)
print(p.full_name)
print(p.__dict__)
p.surname = "Petrov"
print(p.__dict__)
print(p.full_name)

