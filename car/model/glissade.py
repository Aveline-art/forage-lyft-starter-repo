from abc import ABC
from car.car import Car
from engine.model.willoughby_engine import WilloughbyEngine
from battery.model.spindler_battery import SpindlerBattery


class Glissade(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.engine = WilloughbyEngine(
            last_service_mileage, current_mileage)
        self.battery = SpindlerBattery(last_service_date)
        super().__init__(self.engine, self.battery)
