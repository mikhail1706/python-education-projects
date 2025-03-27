class Box[T]:
    def __init__(self) -> None:
        self.value: T | None = None

    def get_value(self) -> T:
        if self.value is None:
            raise ValueError("Box is empty")

        return self.value

    def set_value(self, value: T) -> None:
        self.value = value

class FloatBox(Box[float]):
    pass


def main() -> None:
    int_box: Box[int] = Box()
    int_box.set_value(2)
    print(int_box)

    name_box = Box[str]()
    print(name_box)
    name_box.set_value("Mike")
    name = name_box.get_value()
    print(name)

    pi_box = FloatBox()
    pi_box.set_value(3.14)
    pi = pi_box.get_value()
    print(pi)

if __name__ == '__main__':
    main()
