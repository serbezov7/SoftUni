from project.Core.add_booth import AddBooth
from project.Core.add_delicacy_by_type import AddDelicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []  # Booth objects
        self.delicacies = []  # Delicacy objects
        self.income = 0

        self.add_delicacy_by_type = AddDelicacy()
        self.add_booth_by_type = AddBooth()

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if any(d.name == name for d in self.delicacies):
            raise Exception(f"{name} already exists!")

        delicacy = self.add_delicacy_by_type.create_food(type_delicacy, name, price)

        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if any(b.booth_number == booth_number for b in self.booths):
            raise Exception(f"Booth number {booth_number} already exists!")

        booth = self.add_booth_by_type.create_booth(type_booth, booth_number, capacity)

        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth = self.__find_booth_for_reservation(number_of_people)

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.__find_booth_by_number(booth_number)
        delicacy = self.__find_delicacy_by_name(delicacy_name)

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.__find_booth_by_number(booth_number)
        bill = booth.price_for_reservation + sum(order.price for order in booth.delicacy_orders)

        self.income += bill
        self.clean_booth(booth)
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    def __find_booth_for_reservation(self, number_of_people):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                return booth
        raise Exception(f"No available booth for {number_of_people} people!")

    def __find_booth_by_number(self, number):
        for booth in self.booths:
            if booth.booth_number == number:
                return booth
        raise Exception(f"Could not find booth {number}!")

    def __find_delicacy_by_name(self, name):
        for delicacy in self.delicacies:
            if delicacy.name == name:
                return delicacy
        raise Exception(f"No {name} in the pastry shop!")

    @staticmethod
    def clean_booth(booth):
        booth.delicacy_orders = []
        booth.price_for_reservation = 0
        booth.is_reserved = False

        return booth






