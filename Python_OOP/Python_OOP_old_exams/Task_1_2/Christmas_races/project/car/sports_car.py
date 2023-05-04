from project.car.car import Car


class SportsCar(Car):
    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

    @property
    def get_max_speed(self):
        return 600

    @property
    def get_min_speed(self):
        return 400