"""09. Name mangling"""


from datetime import datetime


import pytz


class Color:
    WHITE = '\u001b[37m'
    GREEN = '\033[0;92m'
    RED = '\033[1;31m'


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self._history = []

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()
        self._history.append(
            [amount, self._get_current_time()]
        )

    def withdrawn(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f'You spent {amount} units')
            self.show_balance()
            self._history.append(
                [-amount, self._get_current_time()]
            )
        else:
            print('Not enough money')
            self.show_balance()

    def show_balance(self):
        print(f'Balance: {self.__balance}')

    def show_history(self):
        for amount, date in self._history:
            if amount > 0:
                transaction = 'deposited'
                color = Color.GREEN
            else:
                transaction = 'withdrawn'
                color = Color.RED
            print(f'{color} {amount} {Color.WHITE} {transaction} on '
                  f'{date.astimezone()}')


class Person:
    __name = 'Mike'


# p = Person()
#
# print(dir(p))


a = Account('Mike', 0)

a.deposit(100)
a.show_balance()

a.__balance = 100000
a.show_balance()
print(a.__dict__)
