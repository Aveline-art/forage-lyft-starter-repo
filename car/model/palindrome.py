from abc import ABC
from car.car import Car
from engine.model.sternman_engine import SternmanEngine
from battery.model.spindler_battery import SpindlerBattery


class Palindrome(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        self.engine = SternmanEngine(
            warning_light_is_on)
        self.battery = SpindlerBattery(last_service_date)
        super().__init__(self.engine, self.battery)
