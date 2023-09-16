from dataclasses import dataclass
from datetime import datetime
from typing import Iterable, Sequence, Mapping


@dataclass
class User:
    birthday: datetime


users = [
    User(birthday=datetime.fromisoformat("1988-01-01")),
    User(birthday=datetime.fromisoformat("1985-07-29")),
    User(birthday=datetime.fromisoformat("2000-10-10")),
]


def get_younger_user(users: list[User]) -> User:
    if not users:
        raise ValueError("empty users!")
    sorted_users = sorted(users, key=lambda u: u.birthday)
    return sorted_users[0]


# User(birthday=datetime.datetime(1985, 7,29, 0, 0))
print(get_younger_user(users))


# Iterable. Итерируемые объекты
def get_younger_user(users: Iterable[User]) -> User | None:
    if not users:
        return None
    sorted_users = sorted(users, key=lambda u: u.birthday)
    return sorted_users[0]


# Sequence. Обращение к элементам по индексу list[1]
def get_younger_user(users: Sequence[User]) -> User | None:
    """Возвращает самого молодого пользователя из списка"""
    if not users:
        return None
    print(users[0])
    sorted_users = sorted(users, key=lambda x: x.birthday)
    return sorted_users[0]


# custom Sequence
class Users:
    def __init__(self, users: Sequence[User]):
        self._users = users

    def __getitem__(self, item: int) -> User:
        return self._users[item]


users = Users(
    (  # сменили на tuple
        User(birthday=datetime.fromisoformat("1988-01-01")),
        User(birthday=datetime.fromisoformat("1985-07-29")),
        User(birthday=datetime.fromisoformat("2000-10-10")),
    )
)
for u in users:
    print(u)


# Mapping. Любая структура к которой можно обращаться по ключам
def smth(some_users: Mapping[str:User]) -> None:
    print(some_users["alex"])


smth(
    {
        "alex": User(birthday=datetime.fromisoformat("1990-01-01")),
        "petr": User(birthday=datetime.fromisoformat("1988-10-23")),
    }
)
