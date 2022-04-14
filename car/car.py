from abc import ABC


class Car(ABC):
    def __init__(self):
        self.engine = None
        self.battery = None

    def needs_service(self):
        if self.engine:
            should_engine = self.engine.needs_service()
        if self.battery:
            should_battery = self.battery.needs_service()
        if should_engine or should_battery:
            return True
