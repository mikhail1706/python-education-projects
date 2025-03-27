def true_div(number: float, divisor: float) -> float:
    return number / divisor


def square(*numbers: int) -> list[int]:
    print(type(numbers))
    return [n * n for n in numbers]


def get_users_by_ids(*user_ids: int | str) -> ...:
    print(type(user_ids))

    for user_id in user_ids:
        if isinstance(user_id, str):
            print(user_id)
        else:
            print(type(user_id))

    return ...


def main():
    print(true_div(10, 4))
    print(true_div(10, 2))
    print(true_div(10.4, 2))
    print(true_div(10.75, 2.5))
    print()
    print(square(1, 2, 3))
    print(square(1, 2, 3))
    print()
    print(get_users_by_ids())
    print(get_users_by_ids(1, 2, 3))
    print(get_users_by_ids("1", "2", "3", 1, 2, 3))
    print()
    data = {'fizz': 'buzz'}
    new_data = {'foo': 'bar', "42": "answer", "first-name": "John Smith"}
    update_data(
        data,
        **new_data,
        spam='eggs',
        number=42,
        ids=(1, 2, 3),
        # names=("Bob", "Alise",)
    )


def update_data(data: dict, **new_data: str | int | tuple[int,...]) -> None:
    data.update(new_data)


if __name__ == '__main__':
    main()
