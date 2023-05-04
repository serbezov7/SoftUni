class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):

    def setUp(self) -> None:
        self.worker = Worker("Ivan", 1000, 100)

    def test_worker_init(self):
        self.assertEqual(self.worker.name, "Ivan")
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 100)
        self.assertEqual(self.worker.money, 0)

    def test_worker_energy_below_zero(self):
        self.worker.energy = -2
        with self.assertRaises(Exception) as error:
            self.worker.work()
        self.assertEqual(str(error.exception), 'Not enough energy.')

    def test_worker_energy_equal_to_zero(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as error:
            self.worker.work()
        self.assertEqual(str(error.exception), 'Not enough energy.')

    def test_salary_increases_money(self):
        self.worker.work()
        self.assertEqual(self.worker.money, 1000)

    def test_energy_decreasing_after_work(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 99)

    def test_rest_increases_energy(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 101)

    def test_get_info_returns_proper_string(self):
        self.assertEqual(self.worker.get_info(), "Ivan has saved 0 money.")


if __name__ == "__main__":
    main()
