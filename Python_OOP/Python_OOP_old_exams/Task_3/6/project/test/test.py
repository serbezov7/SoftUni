from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Name", 2000, 5)

    def test_init(self):
        self.assertEqual(self.movie.name, "Name")
        self.assertEqual(self.movie.year, 2000)
        self.assertEqual(self.movie.rating, 5)

    def test_raises_empty_name(self):
        with self.assertRaises(ValueError) as error:
            self.movie.name = ''
        self.assertEqual(str(error.exception), "Name cannot be an empty string!")

    def test_raises_wrong_year(self):
        with self.assertRaises(ValueError) as error:
            self.movie.year = 1886
        self.assertEqual(str(error.exception), "Year is not valid!")

    def test_adding_actor_correctly(self):
        self.movie.add_actor("Gosho")
        self.assertEqual(1, len(self.movie.actors))
        self.assertEqual("Gosho", self.movie.actors[0])

    def test_raises_when_adding_existing_actor(self):
        self.movie.add_actor("Gosho")
        self.assertEqual(self.movie.add_actor("Gosho"), "Gosho is already added in the list of actors!")

    def test_rating_comparison(self):
        other = Movie("Name2", 2001, 7)
        self.assertEqual(self.movie.__gt__(other), '"Name2" is better than "Name"')

    def test_rating_comparison_first_better_than_other(self):
        other = Movie("Name2", 2001, 3)
        self.assertEqual(self.movie.__gt__(other), '"Name" is better than "Name2"')

    def test_repr_returns_proper_string(self):
        self.movie.actors.append("Gosho")
        self.movie.actors.append("Ivo")
        self.assertEqual("Name: Name\nYear of Release: 2000\nRating: 5.00\nCast: Gosho, Ivo", repr(self.movie))


if __name__ == "__main__":
    main()
