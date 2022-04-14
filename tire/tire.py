from abc import ABC, abstractmethod


class Tire(ABC):
    def __init__(self, sensor_values):
        self.sensor_values = sensor_values

    @abstractmethod
    def needs_service():
        pass
