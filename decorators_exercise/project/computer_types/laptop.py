from project.computer_types.computer import Computer


class Laptop(Computer):

    LAPTOP_PROCESSORS = {
        'AMD Ryzen 9 5950X': 900,
        'Intel Core i9-11900H': 1050,
        'Apple M1 Pro': 1200
    }

    MAX_RAM = 64

    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor, ram):
        if processor not in Laptop.LAPTOP_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        if ram > Laptop.MAX_RAM or not self.check_ram(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        self.ram = ram
        self.processor = processor
        self.price = Laptop.LAPTOP_PROCESSORS[processor] + self.price_ram(ram)

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."

