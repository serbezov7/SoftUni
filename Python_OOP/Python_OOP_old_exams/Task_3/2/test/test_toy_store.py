from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_raises_adding_non_existing_shelf(self):
        with self.assertRaises(Exception) as error:
            self.toy_store.add_toy("Y", "car")
        self.assertEqual(str(error.exception), "Shelf doesn't exist!")

    def test_raises_when_toy_is_in_shelf(self):
        self.toy_store.toy_shelf["A"] = "Car"
        with self.assertRaises(Exception) as error:
            self.toy_store.add_toy("A", "Car")
        self.assertEqual(str(error.exception), "Toy is already in shelf!")

    def test_raises_when_shelf_not_none(self):
        self.toy_store.toy_shelf["A"] = "Car"
        with self.assertRaises(Exception) as error:
            self.toy_store.add_toy("A", "Toy")
        self.assertEqual(str(error.exception), "Shelf is already taken!")

    def test_add_toy_to_shell(self):
        result = self.toy_store.add_toy("A", "Car")
        self.assertEqual(result, "Toy:Car placed successfully!")

    def test_raises_remove_non_existing_shelf(self):
        with self.assertRaises(Exception) as error:
            self.toy_store.remove_toy("Y", "car")
        self.assertEqual(str(error.exception), "Shelf doesn't exist!")

    def test_raises_remove_non_existing_toy(self):
        self.toy_store.toy_shelf["A"] = "Car"
        with self.assertRaises(Exception) as error:
            self.toy_store.remove_toy("A", "Ball")
        self.assertEqual(str(error.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_successfully(self):
        self.toy_store.add_toy("A", "Car")
        result = self.toy_store.remove_toy("A", "Car")
        self.assertEqual(result, "Remove toy:Car successfully!")
        self.assertEqual(None, self.toy_store.toy_shelf["A"])



if __name__ == "__main__":
    main()
