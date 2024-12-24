"""05. Инициализация экземпляров, __init__ метод"""


class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


p = Person('Mike')

print(p.__dict__)
print(p.name)
p.display()
