"""Пример 20.7. bulkfood_v5.py: использование дескрипторов Quantity и NonBlank
в классе LineItem"""


import model_v5 as model    # 1


class LineItem:
    description = model.NonBlank()  # 2
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
