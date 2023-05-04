from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookStore(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(10)

    def test_init(self):
        self.assertEqual(10, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_raises_wrong_book_limit(self):
        with self.assertRaises(ValueError) as error:
            self.bookstore.books_limit = 0
        self.assertEqual(str(error.exception), "Books limit of 0 is not valid")

    def test_len_method(self):
        self.bookstore.availability_in_store_by_book_titles["Book1"] = 3
        self.bookstore.availability_in_store_by_book_titles["Book2"] = 5
        self.assertEqual(8, self.bookstore.__len__())

    def test_receive_raises_when_no_more_space(self):
        self.bookstore.availability_in_store_by_book_titles["Book1"] = 3
        self.bookstore.availability_in_store_by_book_titles["Book2"] = 5

        with self.assertRaises(Exception) as error:
            self.bookstore.receive_book("Book3", 10)
        self.assertEqual(str(error.exception), "Books limit is reached. Cannot receive more books!")

    def test_adding_new_book_to_bookstore(self):
        self.bookstore.availability_in_store_by_book_titles["Book1"] = 3
        result = self.bookstore.receive_book("Book2", 5)
        self.assertEqual(result, "5 copies of Book2 are available in the bookstore.")

    def test_adding_existing_book_to_bookstore(self):
        self.bookstore.availability_in_store_by_book_titles["Book1"] = 3
        result = self.bookstore.receive_book("Book1", 5)
        self.assertEqual(result, "8 copies of Book1 are available in the bookstore.")

    def test_raises_when_try_to_sell_non_existing_book(self):
        self.bookstore.availability_in_store_by_book_titles["Book1"] = 3

        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book("Book2", 1)
        self.assertEqual(str(error.exception), "Book Book2 doesn't exist!")

    def test_raises_when_try_to_sell_more_copies_than_available(self):
        self.bookstore.availability_in_store_by_book_titles["Book1"] = 3

        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book("Book1", 4)
        self.assertEqual(str(error.exception), "Book1 has not enough copies to sell. Left: 3")

    def test_successfully_sell_book(self):
        self.bookstore.availability_in_store_by_book_titles["Book1"] = 3
        result = self.bookstore.sell_book("Book1", 2)
        self.assertEqual(result, "Sold 2 copies of Book1")
        self.assertEqual(1, self.bookstore.availability_in_store_by_book_titles["Book1"])
        self.assertEqual(2, self.bookstore.total_sold_books)

    def test_successfully_sell_all_book(self):
        self.bookstore.availability_in_store_by_book_titles["Book1"] = 3
        result = self.bookstore.sell_book("Book1", 3)
        self.assertEqual(result, "Sold 3 copies of Book1")
        self.assertEqual(0, self.bookstore.availability_in_store_by_book_titles["Book1"])
        self.assertEqual(3, self.bookstore.total_sold_books)

    def test_str_method_returns_proper_string(self):
        self.bookstore.receive_book("Book1", 3)
        self.bookstore.receive_book("Book2", 5)
        self.bookstore.sell_book("Book1", 1)

        result = str(self.bookstore)
        self.assertEqual("Total sold books: 1\nCurrent availability: 7\n - Book1: 2 copies\n - Book2: 5 copies", result)



if __name__ == "__main__":
    main()
