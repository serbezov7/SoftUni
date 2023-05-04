from abc import ABC, abstractmethod
from math import log2, ceil, floor


class Computer(ABC):

    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @property
    @abstractmethod
    def get_processor(self):
        pass

    @property
    @abstractmethod
    def get_ram(self):
        pass

    @property
    @abstractmethod
    def get_type(self):
        pass

    def configure_computer(self, processor, ram):
        if processor not in self.get_processor:
            raise ValueError(f"{processor} is not compatible with {self.get_type} {self.manufacturer} {self.model}!")
        if not self.ram_validation(ram) or ram > self.get_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.get_type} {self.manufacturer} {self.model}!")

        self.price = self.get_price(ram, processor)
        self.processor = processor
        self.ram = ram

        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM " \
               f"for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

    @staticmethod
    def ram_validation(ram):
        result = log2(ram)
        return ceil(result) == floor(result)

    def get_price(self, ram, processor):
        ram_price = int(log2(ram)) * 100
        processor_price = self.get_processor[processor]
        return ram_price + processor_price
