from unittest import TestCase, main

from project.truck_driver import TruckDriver


class TruckDriverTests(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("Gosho", 1)

    def test_proper_init(self):
        self.assertEqual("Gosho", self.driver.name)
        self.assertEqual(1, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_raises_when_negative_earned_money(self):
        with self.assertRaises(ValueError) as error:
            self.driver.earned_money = -3
        self.assertEqual(str(error.exception), f"{self.driver.name} went bankrupt.")

    def test_bankrupt(self):
        self.driver.money_per_mile = 0.01
        self.driver.add_cargo_offer("Plovdiv", 10000)

        with self.assertRaises(ValueError) as error:
            self.driver.drive_best_cargo_offer()

        self.assertEqual(f"{self.driver.name} went bankrupt.", str(error.exception))

    def test_raises_cargo_location_already_added(self):
        self.driver.available_cargos["Sofia"] = 100
        with self.assertRaises(Exception) as error:
            self.driver.add_cargo_offer("Sofia", 100)
        self.assertEqual(str(error.exception), "Cargo offer is already added.")

    def test_cargo_location_proper_added(self):
        self.assertEqual(f"Cargo for 100 to Sofia was added as an offer.", self.driver.add_cargo_offer("Sofia", 100))

    def test_raises_when_no_offers_available(self):
        self.assertEqual(self.driver.drive_best_cargo_offer(), "There are no offers available.")

    def test_earned_money_raises_when_proper_location(self):
        self.driver.available_cargos["Sofia"] = 100
        self.driver.available_cargos["Plovdiv"] = 50

        self.driver.drive_best_cargo_offer()
        self.assertEqual(100, self.driver.earned_money)

    def test_miles_increasing_after_course(self):
        self.driver.available_cargos["Sofia"] = 100
        self.driver.available_cargos["Plovdiv"] = 50

        self.driver.drive_best_cargo_offer()
        self.assertEqual(100, self.driver.miles)

    def test_best_cargo_returns_proper_string(self):
        self.driver.available_cargos["Sofia"] = 100
        self.driver.available_cargos["Plovdiv"] = 50

        self.assertEqual(f"{self.driver.name} is driving 100 to Sofia.", self.driver.drive_best_cargo_offer())

    def test_money_decreasing_when_eat_stop(self):
        self.driver.available_cargos["Sofia"] = 300
        self.driver.drive_best_cargo_offer()

        self.assertEqual(280, self.driver.earned_money)

    def test_money_decreasing_when_sleep_stop(self):
        self.driver.available_cargos["Sofia"] = 1200
        self.driver.drive_best_cargo_offer()

        self.assertEqual(1075, self.driver.earned_money)

    def test_money_decreasing_when_gas_stop(self):
        self.driver.available_cargos["Sofia"] = 1500
        self.driver.drive_best_cargo_offer()

        self.assertEqual(835, self.driver.earned_money)

    def test_money_decreasing_when_repair_stop(self):
        self.driver.available_cargos["Sofia"] = 15000
        self.driver.drive_best_cargo_offer()

        self.assertEqual(625, self.driver.earned_money)

    def test_repr_returns_proper_string(self):
        self.driver.miles = 10000
        self.assertEqual(str(self.driver), "Gosho has 10000 miles behind his back.")


if __name__ == "__main__":
    main()


# from unittest import TestCase
# from project.truck_driver import TruckDriver
#
#
# class TestTruckDriver(TestCase):
#     def setUp(self):
#         self.driver = TruckDriver("Kostadin", 1.40)
#
#     def test_proper_init(self):
#         self.assertEqual(self.driver.name, "Kostadin")
#         self.assertEqual(self.driver.money_per_mile, 1.40)
#         self.assertEqual(self.driver.available_cargos, {})
#         self.assertEqual(self.driver.earned_money, 0)
#         self.assertEqual(self.driver.miles, 0)
#
#     def test_raises_when_negative_earned_money(self):
#         with self.assertRaises(ValueError) as error:
#             self.driver.earned_money = -1
#
#         self.assertEqual(str(error.exception), f"{self.driver.name} went bankrupt.")
#
#     def test_bankrupt(self):
#         self.driver.money_per_mile = 0.01
#         self.driver.add_cargo_offer("California", 2000)
#
#         with self.assertRaises(ValueError) as error:
#             self.driver.drive_best_cargo_offer()
#
#         self.assertEqual(str(error.exception), f"{self.driver.name} went bankrupt.")
#
#     def test_cargo_location_proper_added(self):
#         result = self.driver.add_cargo_offer("California", 2000)
#
#         self.assertEqual(result, f"Cargo for 2000 to California was added as an offer.")
#         self.assertEqual(self.driver.available_cargos, {"California": 2000})
#
#     def test_raises_cargo_location_already_added(self):
#         self.driver.add_cargo_offer("California", 2000)
#
#         with self.assertRaises(Exception) as error:
#             self.driver.add_cargo_offer("California", 2000)
#
#         self.assertEqual(str(error.exception), "Cargo offer is already added.")
#
#     def test_earned_money_raises_when_proper_location(self):
#         self.driver.add_cargo_offer("California", 2000)
#         self.driver.add_cargo_offer("Los Angeles", 20000)
#
#         result = self.driver.drive_best_cargo_offer()
#
#         self.assertEqual(result, f"{self.driver.name} is driving 20000 to Los Angeles.")
#         self.assertEqual(self.driver.earned_money, 4000)
#         self.assertEqual(self.driver.miles, 20000)
#
#     def test_raises_when_no_offers_available(self):
#         result = self.driver.drive_best_cargo_offer()
#         self.assertEqual(result, "There are no offers available.")
#
#     def test_money_decreasing_when_eat_stop(self):
#         self.driver.earned_money = 100
#
#         self.driver.eat(250)
#         self.driver.eat(500)
#
#         self.assertEqual(self.driver.earned_money, 60)
#
#     def test_money_decreasing_when_sleep_stop(self):
#         self.driver.earned_money = 100
#
#         self.driver.sleep(1000)
#         self.driver.sleep(2000)
#
#         self.assertEqual(self.driver.earned_money, 10)
#
#     def test_money_decreasing_when_gas_stop(self):
#         self.driver.earned_money = 2000
#
#         self.driver.pump_gas(1500)
#         self.driver.pump_gas(3000)
#
#         self.assertEqual(self.driver.earned_money, 1000)
#
#     def test_money_decreasing_when_repair_stop(self):
#         self.driver.earned_money = 16000
#
#         self.driver.repair_truck(10000)
#         self.driver.repair_truck(20000)
#
#         self.assertEqual(self.driver.earned_money, 1000)
#
#     def test_repr_returns_proper_string(self):
#         self.assertEqual(str(self.driver), "Kostadin has 0 miles behind his back.")

