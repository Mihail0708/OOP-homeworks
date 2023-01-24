from abc import ABC, abstractmethod

from wild_farm.project.food import Food


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @property
    @abstractmethod
    def food_to_be_eaten(self):
        ...

    @property
    @abstractmethod
    def weight_gain(self):
        ...

    @abstractmethod
    def make_sound(self):
        ...

    def feed(self, food: Food):
        if type(food) not in self.food_to_be_eaten:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += self.weight_gain * food.quantity
        self.food_eaten += food.quantity


class Bird(Animal, ABC):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


