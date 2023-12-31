"""
Basic example showing how to read and validate data from a file using Pydantic.
"""

import json
from typing import Optional

from pydantic import BaseModel, validator, root_validator


class ISBNMissingError(Exception):
    """Custom error that is raised when both ISBN10 and ISBN13 are missing"""

    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message
        super(ISBNMissingError, self).__init__(message)


class ISBN10FormatError(Exception):
    """Custom error that is raised when ISBN10 doesn't have the right format"""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super(ISBN10FormatError, self).__init__(message)


class Book(BaseModel):
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]

    @root_validator(pre=True)
    def check_isbn10_or_isbn13(cls, values):
        if "isbn_10" not in values and "isbn_13" not in values:
            raise ISBNMissingError(
                title=values["title"],
                message="Document should have either an ISBN10 or ISBN13",
            )
        return values

    @validator("isbn_10")
    def isbn_10_valid(cls, value) -> None:
        """Validator to check whether ISBN10 is valid"""
        chars = [c for c in value if c in "0123456789Xx"]
        if len(chars) != 10:
            raise ISBN10FormatError(value=value, message="ISBN10 should be 10 digits.")

        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)

        if sum((10 - i) * char_to_int(x) for i, x in enumerate(chars)) % 11 != 0:
            raise ISBN10FormatError(
                value=value, message="ISBN10 digit sum should be divisible by 11."
            )
        return value

    class Config:
        """Pydantic config class"""

        allow_mutation = False
        anystr_lower = True


def main() -> None:
    """Main function"""

    # Read data from a Json file
    with open("./data.json") as file:
        data = json.load(file)
        books: list[Book] = [Book(**item) for item in data]
        # books[0].title = "my new book"
        # print(books[0].dict(exclude={"price"}))
        # print(books[0].dict(include={"price"}))
        print(books[0].copy(deep=True))


if __name__ == "__main__":
    main()
