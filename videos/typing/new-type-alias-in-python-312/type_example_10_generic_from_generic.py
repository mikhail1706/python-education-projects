from typing import reveal_type


class Storage[T]:
    def __init__(self, value: T) -> None:
        self.value = value


class SuperStorage[V](Storage[V]):
    def multiply(self, times: int) -> list[V]:
        return [self.value] * times


def main():
    foo_storage = Storage[str]("foo")
    reveal_type(foo_storage)

    super_storage = SuperStorage[str]("spam")
    reveal_type(super_storage)
    spams = super_storage.multiply(2)
    print(spams)

    new_supper_storage = SuperStorage(7)
    reveal_type(new_supper_storage)
    spams = new_supper_storage.multiply(2)
    print(spams)


if __name__ == "__main__":
    main()
