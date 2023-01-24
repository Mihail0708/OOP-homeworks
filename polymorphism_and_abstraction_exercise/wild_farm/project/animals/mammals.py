from wild_farm.project.animals.animal import Mammal
from wild_farm.project.food import Fruit, Vegetable, Meat


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def weight_gain(self):
        return 0.10

    @property
    def food_to_be_eaten(self):
        return [Vegetable, Fruit]

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def weight_gain(self):
        return 0.40

    @property
    def food_to_be_eaten(self):
        return [Meat]

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def weight_gain(self):
        return 0.30

    @property
    def food_to_be_eaten(self):
        return [Vegetable, Meat]

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def weight_gain(self):
        return 1.00

    @property
    def food_to_be_eaten(self):
        return [Meat]

    def make_sound(self):
        return "ROAR!!!"

