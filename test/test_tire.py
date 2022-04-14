import unittest

from tire.model.carrigan_tire import CarriganTire
from tire.model.octoprime_tire import OctoprimeTire


class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        sensor_values = [0.9, 0, 0, 0]

        tire = CarriganTire(sensor_values)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        sensor_values = [0.89, 0.89, 0.89, 0.89]

        tire = CarriganTire(sensor_values)
        self.assertFalse(tire.needs_service())


class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        sensor_values = [1, 1, 1, 0]

        tire = OctoprimeTire(sensor_values)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        sensor_values = [1, 1, 0.99, 0]

        tire = OctoprimeTire(sensor_values)
        self.assertFalse(tire.needs_service())


if __name__ == '__main__':
    unittest.main()
