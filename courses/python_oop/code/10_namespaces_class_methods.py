"""10.  Область видимости классов и Методы класса classmethod"""

# local
# Enclosed
# Global
# Builtins


name = 'Ivan'


class Person:
    name = 'Dima'

    @classmethod
    def change_name(cls, name):
        cls.name = name


p = Person()
print(p.__dict__)
p.change_name('class new name')

print('Instance dict: ', p.__dict__)
print('Person.name: ', Person.name)


class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_file(cls, path):
        with open(path) as f:
            name = f.read().strip()

        return cls(name)

    @classmethod
    def from_obj(cls, obj):
        if hasattr(obj, 'name'):
            name = getattr(obj, 'name')
            return cls(name)
        return cls


p = Person('Mike')
print(p.__dict__)

p = Person.from_file('C:/Users/Mike/PycharmProjects/pythonOOP/temp/names.txt')
print(p.__dict__)
print(p.name)


class Config:
    name = 'John'


p = Person.from_obj(Config)
print(p.name)
