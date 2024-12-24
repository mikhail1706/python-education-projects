"""
ISP (Interface Segregation Principle) - Принцип разделения интерфейса
    * Не помещайте слишком много в интерфейс; делите его на отдельные
      интерфейсы
    * <<Вам это никогда не понадобится>> (YAGNI - You Ain't Going Need It)
    * Разделять крупные интерфейсы на мелкие

Идея: не стоит добавлять слишком много программных членов.
      Например: методов в интерфейс

Может показаться хорошей идеей реализовать один большой интерфейс позволив
клиентам реализовать его так как они хотят
"""
from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionPrinter(Machine):
    def print(self, document):
        # ok
        pass

    def fax(self, document):
        pass # noop

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass


class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultifunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)
