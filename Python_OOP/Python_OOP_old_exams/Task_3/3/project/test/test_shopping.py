from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.my_cart = ShoppingCart("Notino", 100)
        self.other_cart = ShoppingCart("Parfum", 100)

    def test_init(self):
        self.assertEqual(self.my_cart.shop_name, "Notino")
        self.assertEqual(self.my_cart.budget, 100)
        self.assertEqual(self.my_cart.products, {})

    def test_wrong_shop_name_raises(self):
        with self.assertRaises(ValueError) as error:
            self.my_cart.shop_name = "notino"

        self.assertEqual(str(error.exception), "Shop must contain only letters and must start with capital letter!")

    def test_raises_adding_product_with_higher_price(self):
        with self.assertRaises(ValueError) as error:
            self.my_cart.add_to_cart("one_million", 100)
        self.assertEqual(str(error.exception), "Product one_million cost too much!")

    def test_adding_product_successfully(self):
        result = self.my_cart.add_to_cart("Voyage", 70)
        self.assertEqual(result, "Voyage product was successfully added to the cart!")
        self.assertEqual({"Voyage": 70}, self.my_cart.products)

    def test_successfully_deleting_product_from_cart(self):
        self.my_cart.add_to_cart("Voyage", 70)
        self.my_cart.add_to_cart("Boss", 50)
        result = self.my_cart.remove_from_cart("Voyage")
        self.assertEqual(result, "Product Voyage was successfully removed from the cart!")
        self.assertEqual({"Boss": 50}, self.my_cart.products)

    def test_raises_when_remove_wrong_product(self):
        with self.assertRaises(ValueError) as error:
            self.my_cart.remove_from_cart("Voyage")
        self.assertEqual(str(error.exception), "No product with name Voyage in the cart!")

    def test_adding_method(self):
        self.my_cart.add_to_cart("Voyage", 70)
        self.other_cart.add_to_cart("Boss", 80)
        merged = self.my_cart.__add__(self.other_cart)

        self.assertEqual("NotinoParfum", merged.shop_name)
        self.assertEqual(200, merged.budget)
        self.assertEqual({"Voyage": 70, "Boss": 80}, merged.products)

    def test_buy_products(self):
        self.my_cart.add_to_cart("Voyage", 70)
        self.my_cart.add_to_cart("Boss", 25)
        result = self.my_cart.buy_products()
        self.assertEqual(result, 'Products were successfully bought! Total cost: 95.00lv.')

    def test_raises_when_sum_is_over_budget(self):
        self.my_cart.add_to_cart("Voyage", 70)
        self.my_cart.add_to_cart("Boss", 40)

        with self.assertRaises(ValueError) as error:
            self.my_cart.buy_products()
        self.assertEqual(str(error.exception), "Not enough money to buy the products! Over budget with 10.00lv!")














if __name__ == "__main__":
    main()
