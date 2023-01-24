from wild_farm.project.animals.animal import Bird
from wild_farm.project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @property
    def weight_gain(self):
        return 0.25

    @property
    def food_to_be_eaten(self):
        return [Meat]

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @property
    def weight_gain(self):
        return 0.35

    @property
    def food_to_be_eaten(self):
        return [Vegetable, Fruit, Seed, Meat]

    def make_sound(self):
        return "Cluck"

