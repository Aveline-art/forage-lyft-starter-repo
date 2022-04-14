from abc import ABC
from car.car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery


class Rorschach(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__()
        self.engine = WilloughbyEngine(
            last_service_mileage, current_mileage)
        self.battery = NubbinBattery(last_service_date)
