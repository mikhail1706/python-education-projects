from dataclasses import dataclass
from datetime import datetime

from enum_expl import WeatherType

# Alias
Celsius = int


@dataclass(slots=True, frozen=True)
class Weather:
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


Phone = str


@dataclass
class User:
    user_id: int
    phone: Phone


def get_user_phone(user: User) -> Phone:
    return user.phone
