# from typing import Generic, TypeVar
#
# T = TypeVar('T')
#
# class Box(Generic[T]):
class Box[T]:
    def __init__(self, value: T) -> None:
        self.value = value

    def get_value(self) -> T:
        return self.value

    def set_value(self, value: T) -> None:
        self.value = value

def main() -> None:
    int_box = Box(5)
    int_box.set_value(2)
    print(int_box)

    name_box = Box("John")
    print(name_box)
    name_box.set_value("Mike")
    name = name_box.get_value()
    print(name)

if __name__ == '__main__':
    main()
