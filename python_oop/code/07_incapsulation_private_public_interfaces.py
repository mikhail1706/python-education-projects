"""7. Инкапсуляция, приватные атрибуты и публичный интерфейс"""


class Person:
    def __init__(self, name, surname):
        self._surname = surname
        self._name = name
        self.name = f'{self._name} {self._surname}'


p = Person('mykhailo', 'humen')
print(p.name)
