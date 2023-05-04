from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class AddDelicacy:
    food_types = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen,
    }

    def create_food(self, food_type, name, price):
        if food_type in self.food_types.keys():
            return self.food_types[food_type](name, price)

        raise Exception(f"{food_type} is not on our delicacy menu!")
