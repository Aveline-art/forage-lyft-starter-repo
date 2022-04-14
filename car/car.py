from abc import ABC


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
        self.parts = [self.engine, self.battery]

    def needs_service(self):
        for part in self.parts:
            if part and part.needs_service():
                return True
        return False
