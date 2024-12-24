from dataclasses import dataclass
from datetime import datetime
from typing import Literal, TypedDict


# Обычный словарь dict
def get_gps_coordinates_dict() -> dict[str, float]:
    return {"longitude": 10, "latitude": 20}


coords = get_gps_coordinates_dict()
print(coords["longitude"])


# Словарь с Literal ключами
def get_gps_coordinates_literal() -> dict[
    Literal["longitude"] | Literal["latitude"], float
]:
    return {"longitude": 10, "latitude": 20}


print(get_gps_coordinates_literal()["longitude"])
print(get_gps_coordinates_literal()["latitude"])  # Тут IDE покажет ошибку!


# TypedDict
class Coordinates(TypedDict):
    longitude: float
    latitude: float


c = Coordinates(longitude=10, latitude=20)
print(c["longitude"], c["longitude"])


# dict with keys as a str and values as a user
@dataclass
class User:
    birthday: datetime


some_users_dict: dict[str, User] = {
    "alex": User(birthday=datetime.fromisoformat("1990-01-01")),
    "petr": User(birthday=datetime.fromisoformat("1988-10-23")),
}
