from collections.abc import Sequence
from typing import reveal_type, TypeAlias

LinesAlias: TypeAlias = Sequence[str]
type Lines = Sequence[str]
reveal_type(LinesAlias)
reveal_type(Lines)

print("LinesAlias", LinesAlias)
print("Lines", Lines)

print("LinesAlias == Sequence[str]", LinesAlias == Sequence[str])
print("Lines == Sequence[str]", Lines == Sequence[str])
print("Lines == LinesAlias", Lines == LinesAlias)

print()
print()

number: TypeAlias = float | int
print(number)
reveal_type(number)

print(isinstance(42, number))
print(isinstance(3.14, number))
print(isinstance(False, number))
print(isinstance("Mike", number))


def make_titles(strings: LinesAlias) -> LinesAlias:
    return [s.title() for s in strings]


def main() -> None:
    names = ["john", "Sam", "Nick"]

    for name in names:
        print(make_titles(name))


if __name__ == "__main__":
    main()
