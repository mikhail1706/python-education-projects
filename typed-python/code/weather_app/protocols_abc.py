from abc import ABC, abstractmethod
from typing import Protocol

from enum_expl import Weather


# abc
class AbstractWeatherStorage(ABC):
    """Interface for any storage saving weather"""

    @abstractmethod
    def save(self, weather: Weather) -> None:
        pass


# Protocol
class WeatherStorage(Protocol):
    """Interface for any storage saving weather"""

    def save(self, weather: Weather):
        pass


class PlainFileWeather:
    def save(self, weather: Weather) -> None:
        print("реализация сохранения погоды")


def save_weather(weather: Weather, storage: WeatherStorage) -> None:
    storage.save(weather)
