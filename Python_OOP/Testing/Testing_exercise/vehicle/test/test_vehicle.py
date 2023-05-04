from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(10, 100)

    def test_class_attributes(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_proper_init(self):
        self.assertEqual(10, self.vehicle.fuel)
        self.assertEqual(10, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)

    def test_raises_when_fuel_not_enough(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(error.exception))

    def test_fuel_decreasing_when_proper_drive(self):
        self.vehicle.fuel = 30
        self.vehicle.drive(20)
        self.assertEqual(5, self.vehicle.fuel)

    def test_raises_when_too_much_fuel(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.refuel(10)
        self.assertEqual(str(error.exception), "Too much fuel")

    def test_refuel_when_proper_refuel(self):
        self.vehicle.drive(5)
        self.vehicle.refuel(5)
        self.assertEqual(8.75, self.vehicle.fuel)

    def test_str_returns_proper_string(self):
        self.assertEqual("The vehicle has 100 horse power with 10 fuel left and"
                         " 1.25 fuel consumption", str(self.vehicle))


if __name__ == "__main__":
    main()
