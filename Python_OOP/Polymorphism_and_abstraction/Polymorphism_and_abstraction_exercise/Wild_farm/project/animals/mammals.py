from abc import ABC, abstractmethod
from project.animals.animal import Mammal


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def weight_increase(self):
        return 0.10

    @property
    def food_to_eat(self):
        return ["Vegetable", "Fruit"]

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def weight_increase(self):
        return 0.40

    @property
    def food_to_eat(self):
        return ["Meat"]

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def weight_increase(self):
        return 0.30

    @property
    def food_to_eat(self):
        return ["Vegetable", "Meat"]

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def weight_increase(self):
        return 1

    @property
    def food_to_eat(self):
        return ["Meat"]

    def make_sound(self):
        return "ROAR!!!"
