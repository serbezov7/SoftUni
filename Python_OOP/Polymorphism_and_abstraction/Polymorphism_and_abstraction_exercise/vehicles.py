from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIR_CONDITIONER = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        self.fuel_consumption += self.AIR_CONDITIONER
        if self.fuel_quantity >= self.fuel_consumption * distance:
            self.fuel_quantity -= self.fuel_consumption * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITIONER = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        self.fuel_consumption += self.AIR_CONDITIONER
        if self.fuel_quantity >= self.fuel_consumption * distance:
            self.fuel_quantity -= self.fuel_consumption * distance

    def refuel(self, fuel):
        new_fuel = fuel * 0.95
        self.fuel_quantity += new_fuel

