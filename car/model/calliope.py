from abc import ABC
from car.car import Car
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery


class Calliope(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.engine = CapuletEngine(
            last_service_mileage, current_mileage)
        self.battery = SpindlerBattery(last_service_date)
        super().__init__(self.engine, self.battery)
