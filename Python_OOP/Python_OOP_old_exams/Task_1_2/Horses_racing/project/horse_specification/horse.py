from abc import ABC, abstractmethod


class Horse(ABC):
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    @abstractmethod
    def get_max_horse_speed(self):
        pass

    @property
    @abstractmethod
    def get_speed_increase(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.get_max_horse_speed:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    def train(self):
        if self.speed + self.get_speed_increase > self.get_max_horse_speed:
            self.speed = self.get_max_horse_speed
        else:
            self.speed += self.get_speed_increase

