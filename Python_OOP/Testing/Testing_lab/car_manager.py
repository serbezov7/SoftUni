class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


from unittest import TestCase, main


class TestCar_manager(TestCase):

    def setUp(self) -> None:
        self.car = Car("Mercedes", "GLS", 12, 100)

    def test_proper_init(self):
        self.assertEqual(self.car.make, "Mercedes")
        self.assertEqual(self.car.model, "GLS")
        self.assertEqual(self.car.fuel_consumption, 12)
        self.assertEqual(self.car.fuel_capacity, 100)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_raise_exception_when_make_null_or_empty(self):
        with self.assertRaises(Exception) as error:
            self.car.make = ""
        self.assertEqual(str(error.exception), "Make cannot be null or empty!")

    def test_raise_exception_when_model_null_or_empty(self):
        with self.assertRaises(Exception) as error:
            self.car.model = ""
        self.assertEqual(str(error.exception), "Model cannot be null or empty!")

    def test_zero_fuel_consumption(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_consumption = 0
        self.assertEqual(str(error.exception), "Fuel consumption cannot be zero or negative!")

    def test_negative_fuel_consumption(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_consumption = -2
        self.assertEqual(str(error.exception), "Fuel consumption cannot be zero or negative!")

    def test_zero_fuel_capacity(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_capacity = 0
        self.assertEqual(str(error.exception), "Fuel capacity cannot be zero or negative!")

    def test_negative_fuel_capacity(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_capacity = -2
        self.assertEqual(str(error.exception), "Fuel capacity cannot be zero or negative!")

    def test_negative_fuel_amount(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_amount = -2
        self.assertEqual(str(error.exception), "Fuel amount cannot be negative!")

    def test_refuel_with_negative_fuel(self):
        with self.assertRaises(Exception) as error:
            self.car.refuel(-3)
        self.assertEqual(str(error.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_with_zero_fuel(self):
        with self.assertRaises(Exception) as error:
            self.car.refuel(0)
        self.assertEqual(str(error.exception), "Fuel amount cannot be zero or negative!")

    def test_fuel_with_correct_values(self):
        self.car.refuel(50)
        self.assertEqual(50, self.car.fuel_amount)

    def test_fuel_with_more_fuel_than_capacity_correct_values(self):
        self.car.refuel(130)
        self.assertEqual(100, self.car.fuel_amount)

    def test_raises_when_fuel_is_not_enough(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_amount = 10
            self.car.drive(100)
        self.assertEqual(str(error.exception), "You don't have enough fuel to drive!")

    def test_lower_the_fuel_when_fuel_is_enough(self):
        self.car.fuel_amount = 15
        self.car.drive(100)
        self.assertEqual(3, self.car.fuel_amount)


if __name__ == "__main__":
    main()
