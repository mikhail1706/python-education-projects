class Pair[K, V]:
    def __init__(self, first: K, second: V) -> None:
        self.first = first
        self.second = second

    def get_key(self) -> K:
        return self.first

    def get_value(self) -> V:
        return self.second


def main() -> None:
    pair_one = Pair[str, int]("one", 1)
    key = pair_one.get_key()
    value = pair_one.get_value()
    print(key, value)

    pair_two = Pair("two", 2)
    key = pair_two.get_key()
    value = pair_two.get_value()
    print(key, value)

    pair_two = Pair("foo", "bar")
    key = pair_two.get_key()
    value = pair_two.get_value()
    print(key, value)

if __name__ == '__main__':
    main()
