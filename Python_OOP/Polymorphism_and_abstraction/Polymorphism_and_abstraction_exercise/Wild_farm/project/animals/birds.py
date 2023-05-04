from project.animals.animal import Bird


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @property
    def weight_increase(self):
        return 0.25

    @property
    def food_to_eat(self):
        return ["Meat"]

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @property
    def weight_increase(self):
        return 0.35

    @property
    def food_to_eat(self):
        return ["Vegetable", "Fruit", "Meat", "Seed"]

    def make_sound(self):
        return "Cluck"
