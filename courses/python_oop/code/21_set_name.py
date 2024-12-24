"""21. Метод __set_name__ и хранение данных в экземпляре класса-владельца
"""


class ValidateString:
    def __set_name__(self, owner, name):
        self.property_name = name

    def __set__(self, instance, value):
        print('__set__ was called')
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a String, '
                             f'but type: {type(value).__name__} was passed')
        # key = f'_{self.property_name}'
        # setattr(instance, key, value)
        instance.__dict__[self.property_name] = value

    def __get__(self, instance, owner):
        print('__get__ was called')
        if instance is None:
            return self

        # key = f'_{self.property_name}'
        # return getattr(instance, key)
        return instance.__dict__.get(self.property_name, None)


class Person:
    name = ValidateString()
    surname = ValidateString()


p = Person()
p.name = 'Mykhailo'
p.surname = 'Humen'

print(p.__dict__)

print(p.name)
print(p.surname)