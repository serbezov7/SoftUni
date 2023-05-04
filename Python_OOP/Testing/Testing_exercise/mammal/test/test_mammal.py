from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Kitty", "Cat", "mrr")

    def test_proper_init(self):
        self.assertEqual("Kitty", self.mammal.name)
        self.assertEqual("Cat", self.mammal.type)
        self.assertEqual("mrr", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_returns_proper_string(self):
        self.assertEqual("Kitty makes mrr", self.mammal.make_sound())

    def test_get_kingdom_returns_proper_result(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_returns_proper_string(self):
        self.assertEqual("Kitty is of type Cat", self.mammal.info())


if __name__ == "__main__":
    main()