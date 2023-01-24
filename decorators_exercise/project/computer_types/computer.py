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
        if value.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == "":
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @staticmethod
    def price_ram(n):
        return int(log2(n)) * 100

    @staticmethod
    def check_ram(n):
        ram = log2(n)
        return ceil(ram) == floor(ram)

    @abstractmethod
    def configure_computer(self, processor, ram):
        ...

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
