from abc import ABC
from datetime import datetime
from battery.battery import Battery


class SpindlerBattery(Battery, ABC):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)

    def needs_service(self):
        return datetime.today().date() > self.last_service_date.replace(year=self.last_service_date.year + 3)
