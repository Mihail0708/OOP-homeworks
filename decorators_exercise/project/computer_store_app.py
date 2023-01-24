from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer, manufacturer, model, processor, ram):
        if type_computer == 'Desktop Computer':
            computer = DesktopComputer(manufacturer, model)

        elif type_computer == 'Laptop':
            computer = Laptop(manufacturer, model)

        else:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        result = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return result

    def sell_computer(self, client_budget, wanted_processor, wanted_ram):
        for item in self.warehouse:
            if item.price <= client_budget and item.processor == wanted_processor and item.ram >= wanted_ram:
                self.profits += client_budget - item.price
                self.warehouse.remove(item)

                return f"{item} sold for {client_budget}$."

            raise Exception("Sorry, we don't have a computer for you.")


computer_store = ComputerStoreApp()
print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))




