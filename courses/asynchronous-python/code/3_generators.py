"""Пример асинхронности на генераторах. Событий цикл
   по принципу Round Robin (Карусель)

    1. Генераторы - это функции, которые возвращают какой-то результат
    2. yield в - одной функции может быть несколько
    3. Функция next сдвигает выполнение программы до след. yield"""

from time import time


# g = gen('Oleg')


def get_file_name():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)
        yield pattern.format(str(t))


def gen1(s):
    for i in s:
        yield i


def gen2(n):
    for i in range(n):
        yield i


g1 = gen1('oleg')
g2 = gen2(4)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
