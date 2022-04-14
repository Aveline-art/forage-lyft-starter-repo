from pickle import FALSE
import unittest

from car.car import Car


class TestCar(unittest.TestCase):
    def test_car_should_be_serviced(self):
        class Object:
            def needs_service(self):
                return True

        engine = Object()
        battery = Object()
        tire = Object()
        car = Car(engine, battery, tire)
        self.assertTrue(car.needs_service())

    def test_car_should_not_be_serviced(self):
        car = Car()
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
