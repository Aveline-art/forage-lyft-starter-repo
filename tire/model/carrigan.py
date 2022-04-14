from abc import ABC
from tire.tire import Tire


class CarriganTire(Tire, ABC):
    def __init__(self, sensor_values):
        super().__init__(sensor_values)

    def needs_service(self):
        return any([value >= 0.9 for value in self.sensor_values])
