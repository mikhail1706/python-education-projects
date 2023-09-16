
import asyncio
from time import time


@asyncio.coroutine
def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        yield from asyncio.sleep(1)


@asyncio.coroutine
def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f'{count} seconds have passed')
        count += 1
        yield from asyncio.sleep(1)


@asyncio.coroutine
def main():
    task_1 = asyncio.ensure_future(print_nums())
    task_2 = asyncio.ensure_future(print_time())

    yield from asyncio.gather(task_1, task_2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

