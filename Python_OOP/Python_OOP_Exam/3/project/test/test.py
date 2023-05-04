from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("Gosho", 32, 250)
        self.other = TennisPlayer("Ivan", 24, 150)

    def test_init(self):
        self.assertEqual("Gosho", self.player.name)
        self.assertEqual(32, self.player.age)
        self.assertEqual(250, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_raises_when_short_name(self):
        with self.assertRaises(ValueError) as error:
            self.player.name = "Iv"
        self.assertEqual(str(error.exception), "Name should be more than 2 symbols!")

    def test_raises_when_under_18(self):
        with self.assertRaises(ValueError) as error:
            self.player.age = 14
        self.assertEqual(str(error.exception), "Players must be at least 18 years of age!")

    def test_adding_new_win_properly(self):
        self.player.add_new_win("Australian Open")
        self.assertEqual(len(self.player.wins), 1)
        self.assertEqual("Australian Open", self.player.wins[0])

    def test_raises_when_tournament_in_wins(self):
        self.player.add_new_win("Australian Open")
        result = self.player.add_new_win("Australian Open")

        self.assertEqual(result, "Australian Open has been already added to the list of wins!")

    def test_lt_method_works_correct(self):
        result = self.player.__lt__(self.other)

        self.assertEqual(result, 'Gosho is a better player than Ivan')

    def test_lt_method_returns_when_other_player_is_better(self):
        self.other.points = 350
        result = self.player.__lt__(self.other)

        self.assertEqual(result, "Ivan is a top seeded player and he/she is better than Gosho")

    def test_str_method_returns_proper_string(self):
        self.player.add_new_win("Australian Open")
        self.player.add_new_win("Tournament2")

        self.assertEqual("Tennis Player: Gosho\nAge: 32\nPoints: 250.0\nTournaments won: Australian Open, Tournament2",
                         str(self.player))


if __name__ == "__main__":
    main()
