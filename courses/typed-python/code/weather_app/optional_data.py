# optional params
def print_hello(name: str | None = None) -> None:
    print(f"Hello {name}" if name is not None else "Hello anon!")


# tuple with limited length
three_ints = tuple[int, int, int]

# tuple with undefined length
tuple_ints = tuple[int, ...]
