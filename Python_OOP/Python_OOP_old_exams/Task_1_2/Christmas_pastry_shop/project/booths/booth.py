from abc import ABC, abstractmethod


class Booth(ABC):
    def __init__(self, booth_number, capacity):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders = []  # ordered Delicacy objects
        self.price_for_reservation = 0
        self.is_reserved = False

    @property
    @abstractmethod
    def get_price(self):
        pass

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")
        self.__capacity = value

    def reserve(self, number_of_people):
        reservation_price = self.get_price * number_of_people
        self.price_for_reservation = reservation_price
        self.is_reserved = True

