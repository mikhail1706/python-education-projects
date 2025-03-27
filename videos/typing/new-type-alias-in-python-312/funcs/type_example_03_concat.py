
def concatenate[T: (str, bytes)](left: T, right:T) ->T:
    return left + right

def main() -> None:
    foobar = concatenate("foo", "bar")
    print(foobar)
    spameggs = concatenate(b"spam", b"spam")
    print(spameggs)


if __name__ == '__main__':
    main()
