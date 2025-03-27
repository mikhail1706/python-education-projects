import random
from typing import Sequence, TypeVar


T = TypeVar("T")


def get_random_element(items: Sequence[T]) -> T:
    return random.choice(items)


def main() -> None:
    num = get_random_element([1, 2, 3, 4, 5])
    print(num)
    names =  get_random_element(["john", "Sam", "Nick"])
    print(names)


if __name__ == '__main__':
    main()
