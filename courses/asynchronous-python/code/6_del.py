"""
Делегирующий генератор, тот который вызывает другой гинератор.
Подгенератор - вызываемый генератор.
Делегирующий блокируется, пока не отрабатывает под делигато
yield from
"""


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class BlaBlaException(Exception):
    pass


def sub_gen():
    while True:
        try:
            message = yield
        except StopIteration:
            # print('Ku-ku!!!')
            break
        else:
            print('.........', message)

    return 'Return'


@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)
    result = yield from g
    print(result)
