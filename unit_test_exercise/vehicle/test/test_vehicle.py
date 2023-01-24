from unittest import TestCase, main
from vehicle.project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(50.0, 250.0)

    def test_default_fuel_consumption_correct(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_initialization(self):
        self.assertEqual(50.0, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(250.0, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_raise_exception_when_drive_with_less_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_correct(self):
        self.vehicle.drive(10)
        self.assertEqual(37.5, self.vehicle.fuel)

    def test_raise_exception_when_refuel_with_more_fuel(self):
        self.vehicle.capacity = 40
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(50)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_correct_refuel(self):
        self.vehicle.fuel = 30
        self.vehicle.refuel(10)
        self.assertEqual(40, self.vehicle.fuel)

    def test_str_represent(self):
        result = self.vehicle
        self.assertEqual("The vehicle has 250.0 horse power with 50.0 fuel left and 1.25 fuel consumption", str(result))


if __name__ == '__main__':
    main()