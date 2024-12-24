from typing import NamedTuple


# NamedTuple
class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using MacBook GPS"""
    return Coordinates(10, 20)


coordinates = get_gps_coordinates()
print(f"Широта:", coordinates.latitude)  # Печать широты
print(f"Долгота:", coordinates.longitude)

latitude, longitude = get_gps_coordinates()
coordinates = get_gps_coordinates()
coordinates.latitude = 10  # IDE подсветит ошибку тут
