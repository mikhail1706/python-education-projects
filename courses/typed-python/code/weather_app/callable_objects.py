from typing import Callable


# Callable
def my_sum(a: int, b: int) -> int:
    return a + b


def process_operation(operation: Callable[[int, int], int], a: int, b: int) -> int:
    return operation(a, b)


print(process_operation(my_sum, 1, 5))  # 6
