class IntegerList:

    def __init__(self, *args):
        self.__integers = []
        for x in args:
            if type(x) == int:
                self.__integers.append(x)

    def get_data(self):
        return self.__integers

    def add(self, element):
        if not isinstance(element, int):
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index not in range(len(self.__integers)):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index not in range(len(self.__integers)):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, element):
        if index not in range(len(self.__integers)):
            raise IndexError("Index is out of range")
        if not isinstance(element, int):
            raise ValueError("Element is not Integer")
        self.get_data().insert(index, element)

    def get_biggest(self):
        return max(self.__integers)

    def get_index(self, element):
        return self.get_data().index(element)


from unittest import TestCase, main


class TestIntegers(TestCase):
    def setUp(self) -> None:
        self.integer_list = IntegerList("30", 10, "Iven", 100, 15, 39)

    def test_proper_init(self):
        self.assertEqual([10, 100, 15, 39], self.integer_list.get_data())

    def test_adds_element_to_list(self):
        self.integer_list.add(5)
        self.assertEqual([10, 100, 15, 39, 5], self.integer_list.get_data())

    def test_raises_when_el_is_not_int(self):
        with self.assertRaises(ValueError) as error:
            self.integer_list.add("Ivan")
        self.assertEqual(str(error.exception), "Element is not Integer")

    def test_removes_element_on_correct_index(self):
        self.integer_list.remove_index(1)
        self.assertEqual([10, 15, 39], self.integer_list.get_data())

    def test_removes_element_on_incorrect_index(self):
        with self.assertRaises(IndexError) as error:
            self.integer_list.remove_index(6)
        self.assertEqual(str(error.exception), "Index is out of range")

    def test_get_by_correct_index(self):
        self.assertEqual(100, self.integer_list.get(1))

    def test_get_by_incorrect_index(self):
        with self.assertRaises(IndexError) as error:
            self.integer_list.get(7)
        self.assertEqual(str(error.exception), "Index is out of range")

    def test_insert_correct_value_on_correct_index(self):
        self.integer_list.insert(1, 23)
        self.assertEqual([10, 23, 100, 15, 39], self.integer_list.get_data())

    def test_insert_correct_value_on_incorrect_index(self):
        with self.assertRaises(IndexError) as error:
            self.integer_list.insert(9, 19)
        self.assertEqual(str(error.exception), "Index is out of range")

    def test_insert_incorrect_value_on_correct_index(self):
        with self.assertRaises(ValueError) as error:
            self.integer_list.insert(2, "Test")
        self.assertEqual(str(error.exception), "Element is not Integer")

    def test_get_biggest(self):
        self.assertEqual(100, self.integer_list.get_biggest())

    def test_get_index_by_element(self):
        self.assertEqual(1, self.integer_list.get_index(100))



if __name__ == "__main__":
    main()
