from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []  # Meals objects
        self.clients_list = []  # Clients objects

    def register_client(self, client_phone_number: str):
        if any(c.phone_number == client_phone_number for c in self.clients_list):
            raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ not in ["Starter", "MainDish", "Dessert"]:
                continue
            self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        result = ""
        for menu in self.menu:
            result += menu.details() + "\n"
        return result.strip()

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        if not any(c.phone_number == client_phone_number for c in self.clients_list):
            self.register_client(client_phone_number)
        client = self.__find_client_by_phone_number(client_phone_number)

        meals_to_order = []
        current_bill = 0

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= meal_quantity:
                        meals_to_order.append(meal)
                        current_bill += meal.price * meal_quantity
                        break
                    else:
                        raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")
            else:
                raise Exception(f"{meal_name} is not on the menu!")

        client.shopping_cart.extend(meals_to_order)
        client.bill += current_bill

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= meal_quantity

            if meal_name not in client.orders:
                client.orders[meal_name] = 0
            client.orders[meal_name] += meal_quantity

        return f"Client {client_phone_number} " \
               f"successfully ordered {', '.join(meal.name for meal in client.shopping_cart)} " \
               f"for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__find_client_by_phone_number(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for meal in self.menu:
            for name, quantity in client.orders.items():
                if meal.name == name:
                    meal.quantity += quantity

        client.shopping_cart = []
        client.bill = 0
        client.orders = {}
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__find_client_by_phone_number(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill
        client.shopping_cart = []
        client.bill = 0
        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} was successfully paid" \
               f" for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    def __find_client_by_phone_number(self, number):
        for client in self.clients_list:
            if client.phone_number == number:
                return client

