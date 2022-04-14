from abc import ABC
from tire.tire import Tire


class OctoprimeTire(Tire, ABC):
    def __init__(self, sensor_values):
        super().__init__(sensor_values)

    def needs_service(self):
        return sum(self.sensor_values) >= 3
