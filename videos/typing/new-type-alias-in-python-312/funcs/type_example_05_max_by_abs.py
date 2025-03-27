from typing import Sequence, SupportsAbs, reveal_type


def make_abs[T: SupportsAbs[float]](*values: T) -> T:
    return max(values, key=abs)

def main() -> None:
    max_num = make_abs(1, 2, 3, 4)
    reveal_type(max_num)
    print(max_num)




if __name__ == '__main__':
    main()
