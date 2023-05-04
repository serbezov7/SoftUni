from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(20)

    def test_init(self):
        self.assertEqual(20, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_setter_raises_when_negative_value(self):
        with self.assertRaises(ValueError) as error:
            self.plantation.size = -3
        self.assertEqual(str(error.exception), "Size must be positive number!")

    def test_raises_when_hire_existing_worker(self):
        self.plantation.workers.append("Miro")
        with self.assertRaises(ValueError) as error:
            self.plantation.hire_worker("Miro")
        self.assertEqual(str(error.exception), "Worker already hired!")

    def test_hire_worker_successfully(self):
        result = self.plantation.hire_worker("Miro")
        self.assertEqual(result, "Miro successfully hired.")
        self.assertEqual(1, len(self.plantation.workers))

    def test_len_method(self):
        self.plantation.plants = {"Miro": ["Flower1", "Flower2"], "Gosho": ["Flower3", "Flower4"]}
        self.assertEqual(self.plantation.__len__(), 4)

    def test_raises_non_existing_worker(self):
        with self.assertRaises(ValueError) as error:
            self.plantation.planting("Miro", "Flower1")
        self.assertEqual(str(error.exception), "Worker with name Miro is not hired!")

    def test_raises_when_plantation_is_full(self):
        self.plantation.hire_worker("Miro")
        self.plantation.size = 2
        self.plantation.plants = {"Miro": ["Flower1", "Flower2"]}
        with self.assertRaises(ValueError) as error:
            self.plantation.planting("Miro", "Flower3")
        self.assertEqual(str(error.exception), "The plantation is full!")

    def test_existing_worker_planting_more_than_one_flower(self):
        self.plantation.hire_worker("Miro")
        self.plantation.plants = {"Miro": ["Flower1", "Flower2"]}
        result = self.plantation.planting("Miro", "Flower3")

        self.assertEqual(result, "Miro planted Flower3.")
        self.assertEqual("Flower3", self.plantation.plants["Miro"][-1])
        self.assertEqual(3, len(self.plantation.plants["Miro"]))

    def test_worker_plants_first_flower(self):
        self.plantation.hire_worker("Miro")
        result = self.plantation.planting("Miro", "Flower1")

        self.assertEqual(result, "Miro planted it's first Flower1.")
        self.assertEqual("Flower1", self.plantation.plants["Miro"][0])
        self.assertEqual(1, len(self.plantation.plants["Miro"]))

    def test_str_method_returns_proper_string(self):
        self.plantation.hire_worker("Miro")
        self.plantation.hire_worker("Gosho")
        self.plantation.plants = {"Miro": ["Flower1", "Flower2"], "Gosho": ["Flower3", "Flower4"]}

        self.assertEqual("Plantation size: 20\nMiro, Gosho\nMiro planted: Flower1, Flower2\n"
                         "Gosho planted: Flower3, Flower4", str(self.plantation))

    def test_repr_returns_proper_string(self):
        self.plantation.hire_worker("Miro")
        self.plantation.hire_worker("Gosho")
        self.plantation.plants = {"Miro": ["Flower1", "Flower2"], "Gosho": ["Flower3", "Flower4"]}

        self.assertEqual("Size: 20\nWorkers: Miro, Gosho", repr(self.plantation))


if __name__ == "__main__":
    main()
