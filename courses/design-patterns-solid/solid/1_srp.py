"""
SRP (Single Responsibility Principle) - принцип единственной ответственности
    * У класса должна быть только одна причина для изменения
    * разделение ответственностей - разные классы обрабатывают разные,
      независимые задачи и проблемы

Идея: если у вас есть класс у этого класса должна быть своя основная
      ответственность. Он не должен брать на себя другие ответственности

PS: Не стоит перегружать свои объекты большим количеством обязанностей

Антипатерн: god object (всемогущий объект) все что есть собрать
            в один класс
"""


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def load_from_web(self, uri):
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('I cried today')
j.add_entry('I ate a bug')
print(f'Journal entries: \n{j}')

file = b'C:/Users/Mike/PycharmProjects/designPatterns/temp/journal.txt'
PersistenceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())
