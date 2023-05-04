from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    def __init__(self, name, speed):
        super().__init__(name, speed)

    @property
    def get_max_horse_speed(self):
        return 140

    @property
    def get_speed_increase(self):
        return 3