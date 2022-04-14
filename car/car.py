from abc import ABC


class Car(ABC):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire
        self.parts = [self.engine, self.battery, self.tire]

    def needs_service(self):
        for part in self.parts:
            if hasattr(part, 'needs_service') and part.needs_service():
                return True
        return False
