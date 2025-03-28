"""
    Абстрактная фабрика
"""
from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('This tea is delicious')


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print('Put in tea bag, boil water',
              f' pour {amount}ml, enjoy')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print('Grind some beans, beans water,', f'pour {amount}, ml, enjoy!')
        return Coffee()


def make_drink(type):
    if type == 'tea':
        return TeaFactory().prepare(200)
    elif type == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = f'{name}Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available Drinks:')
        for f in self.factories:
            print(f[0])

        s = input(f'Please pick dink (0-{len(self.factories)-1}): ')
        idx = int(s)
        s = input('Specify amount: ')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


if __name__ == '__main__':
    hdm = HotDrinkMachine()
    hdm.make_drink()
