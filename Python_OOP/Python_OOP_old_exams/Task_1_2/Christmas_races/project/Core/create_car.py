from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class AddCar:
    models = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar
    }

    def adding_new_car(self, car_type, model, speed_limit):
        if car_type in self.models:
            return self.models[car_type](model, speed_limit)