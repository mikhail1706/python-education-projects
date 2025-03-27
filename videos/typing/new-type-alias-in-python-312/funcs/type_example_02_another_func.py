def repeat[T](val: T, times: int) -> list[T]:
    return [val] * times


def main() -> None:
    nums = repeat(5, 10)
    print(nums)
    words = repeat("word", 3)
    print(words)
    pairs = repeat((4,2), 3)
    print(pairs)
    pairs_2 = repeat((4, "2"), 3)
    print(pairs_2)


if __name__ == '__main__':
    main()
