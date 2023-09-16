from dataclasses import dataclass


# Dataclass
@dataclass
class Coordinates:
    longitude: float
    latitude: float


def get_gps_coordinates_class() -> Coordinates:
    return Coordinates(10, 20)


print(get_gps_coordinates_class().latitude)
print(get_gps_coordinates_class().longitude)


# Frozen dataclass
@dataclass(slots=True, frozen=True)
class CoordinatesDT2:
    longitude: float
    latitude: float


coordinates_dt2 = CoordinatesDT2(longitude=10.0, latitude=20.0)
print("Dataclass with frozen and slots")
