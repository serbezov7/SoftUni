class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


from unittest import TestCase, main


class CatTests(TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Kitty")

    def test_proper_init(self):
        self.assertEqual(self.cat.name, "Kitty")
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(self.cat.size, 0)

    def test_exception_when_is_already_eaten(self):
        self.cat.eat()
        with self.assertRaises(Exception) as error:
            self.cat.eat()
        self.assertEqual(str(error.exception), 'Already fed.')

    def test_is_fed_when_eats(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_is_sleepy_when_fed(self):
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)

    def test_size_increase_when_eat(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_sleep_raises_exception_when_is_hungry(self):
        with self.assertRaises(Exception) as error:
            self.cat.sleep()
        self.assertEqual(str(error.exception), 'Cannot sleep while hungry')

    def test_going_to_sleep_when_fed(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
