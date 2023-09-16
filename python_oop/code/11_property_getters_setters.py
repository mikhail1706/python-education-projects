"""11.Свойства  property, геттеры и сеттеры (getter, setter)"""


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        print('From set_name()')
        self._name = value

    # name = name.setter(set_name)
    # name = property(name)

    # def get_name(self):
    #     print('From get_name()')
    #     return self._name

    # name = property(fget=get_name, fset=set_name)
    # name = property()
    # name = name.getter(get_name)
    # name = name.setter(set_name)


p = Person('John')
print(p.__dict__)
print(p.name)
p.name = 'Mike'
print(p.__dict__)
