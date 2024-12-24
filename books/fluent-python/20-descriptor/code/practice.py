"""20. Дескрипторы атрибутов

    Переопределяющие дескрипторы
    bulkfood_v3.py
    Пример 20.1. bulkfood_v3.py: дескрипторы Quantity управляют
                 атрибутами LineItem

    bulkfood_v4.py
    Пример 20.2. bulkfood_v4.py: каждый дескриптор Quantity получает уникальное
                 имя storage_name
    Пример 20.3. bulkfood_v4b.py (неполный листинг): при вызове через
                 управляемый класс метод __get__ возвращает ссылку
                 на сам дескриптор

    bulkfood_v4c.py
    Пример 20.4. bulkfood_v4c.py: ничем не загроможденное определение LineItem;
                 дескрипторный класс Quantity теперь находится в импортируемом
                 модуле model_v4c

    bulkfood_v4prop.py
    Пример 20.5. bulkfood_v4prop.py: та же функциональность,
                 что в примере 20.2, но реализованная в виде фабрики свойств,
                 а не дескрипторного класса

    model_v5.py
    Пример 20.6. model_v5.py: дескрипторные классы после рефакторинга

    bulkfood_v5.py
    Пример 20.7. bulkfood_v5.py: использование дескрипторов Quantity и NonBlank
                 в классе LineItem

    Непереопределяющие
    descriptorkinds.py
    Пример 20.8. descriptorkinds.py: простые классы для изучения поведения
                 переопределяющих и непереопределяющих дескрипторов

    Пример 20.9. Поведение переопределяющего дескриптора: obj.over – экземпляр
                 класса Overriding (из примера 20.8)

    method_is_descriptor.py
    Пример 20.14. method_is_descriptor.py: класс Text, наследующий UserString
    Пример 20.15. Эксперименты с методом
"""
