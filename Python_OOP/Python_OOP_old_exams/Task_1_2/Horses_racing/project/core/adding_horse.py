from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class AddHorse:
    valid_types = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred,
    }

    def adding_horse(self, type, name, speed):
        if type in self.valid_types:
            horse = self.valid_types[type](name, speed)
            return horse