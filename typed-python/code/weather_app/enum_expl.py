from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from dataclass_types import Coordinates


# Alias and Enum
class WeatherType(str, Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"


Celsius = int


@dataclass(slots=True, frozen=True)
class Weather:
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(coordinates: Coordinates) -> Weather:
    """Requests weather in OpenWeather API and returns it"""
    return Weather(
        temperature=20,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat("2022-05-04 04:00:00"),
        sunset=datetime.fromisoformat("2022-05-04 20:25:00"),
        city="Moscow",
    )


print(WeatherType.CLEAR)  # WeatherType.CLEAR
print(WeatherType.CLEAR.value)  # Ясно
print(WeatherType.CLEAR.name)  # CLEAR


def print_weather_type(weather_type: WeatherType) -> None:
    print(weather_type.value)


print_weather_type(WeatherType.CLOUDS)
print(isinstance(WeatherType.CLOUDS, WeatherType))  # True

# по Enum можно итерироваться в цикле,
for weather_type in WeatherType:
    print(weather_type.name, weather_type.value)


# Enum структуру можно разбирать с помощью новых возможностей Python
# — Pattern Matching:
def what_should_i_do(weather_type: WeatherType) -> None:
    match weather_type:
        case WeatherType.THUNDERSTORM | WeatherType.RAIN:
            print("Уф, лучше сиди дома")
        case WeatherType.CLEAR:
            print("О, отличная погодка")
        case _:
            print("Ну так, выходить можно")


what_should_i_do(WeatherType.CLOUDS)  # Ну так, выходить можно


# Наследование от str и Enum
class WeatherTypeStrEnum(str, Enum):
    FOG = "Туман"
    CLOUDS = "Облачно"


# Вариант без наследования от str
class WeatherTypeEnum(Enum):
    FOG = "Туман"
    CLOUDS = "Облачно"


print(WeatherTypeStrEnum.CLOUDS.upper())  # ОБЛАЧНО
print(WeatherTypeEnum.CLOUDS.upper())  # AttributeError
print(WeatherTypeEnum.CLOUDS.value.upper())  # ОБЛАЧНО

print(WeatherTypeStrEnum.CLOUDS == "Облачно")  # True
print(WeatherTypeEnum.CLOUDS == "Облачно")  # False
print(WeatherTypeEnum.CLOUDS.value == "Облачно")  # True

print(f"Погода: {WeatherTypeStrEnum.CLOUDS}")  # Погода: Облачно
print(f"Погода: {WeatherTypeEnum.CLOUDS}")  # Погода: WeatherTypeEnum.CLOUDS
print(f"Погода: {WeatherTypeEnum.CLOUDS.value}")  # Погода: Облачно


def make_something_great_with_weather(weather: WeatherTypeStrEnum):
    pass


make_something_great_with_weather("Туман")  # Не пройдёт проверку типов
make_something_great_with_weather(WeatherTypeStrEnum.FOG)  # Ок, всё в порядке
