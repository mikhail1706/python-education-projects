from typing import TypeVar, Iterable

# Generics
T = TypeVar("T")


def first(iterable: Iterable[T]) -> T | None:
    for element in iterable:
        return element


print(first(["one", "two"]))  # one
print(first((100, 200)))  # 100
