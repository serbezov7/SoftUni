from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, model, speed_limit):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    @abstractmethod
    def get_max_speed(self):
        pass

    @property
    @abstractmethod
    def get_min_speed(self):
        pass

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if not self.get_min_speed <= value <= self.get_max_speed:
            raise ValueError(f"Invalid speed limit! Must be between {self.get_min_speed} and {self.get_max_speed}!")
        self.__speed_limit = value

