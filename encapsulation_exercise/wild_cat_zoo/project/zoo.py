from wild_cat_zoo.project.animal import Animal
from wild_cat_zoo.project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if self.__budget < price:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_worker = 0
        for worker in self.workers:
            sum_worker += worker.salary

        if self.__budget >= sum_worker:
            self.__budget -= sum_worker
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_animal = 0
        for animal in self.animals:
            sum_animal += animal.money_for_care

        if self.__budget >= sum_animal:
            self.__budget -= sum_animal
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals = [animal.__class__.__name__ for animal in self.animals]
        lion = animals.count('Lion')
        tiger = animals.count('Tiger')
        cheetah = animals.count('Cheetah')
        sep = '\n'

        return f"You have {len(self.animals)} animals\n" \
            f"----- {lion} Lions:\n" \
            f"{sep.join([str(el) for el in self.animals if el.__class__.__name__ == 'Lion'])}\n" \
            f"----- {tiger} Tigers:\n" \
            f"{sep.join([str(el) for el in self.animals if el.__class__.__name__ == 'Tiger'])}\n" \
            f"----- {cheetah} Cheetahs:\n" \
            f"{sep.join([str(el) for el in self.animals if el.__class__.__name__ == 'Cheetah'])}"

    def workers_status(self):
        workers = [worker.__class__.__name__ for worker in self.workers]
        keepers = workers.count('Keeper')
        caretaker = workers.count('Caretaker')
        vet = workers.count('Vet')
        sep = '\n'

        return f"You have {len(self.workers)} workers\n" \
               f"----- {keepers} Keepers:\n" \
               f"{sep.join([str(el) for el in self.workers if el.__class__.__name__ == 'Keeper'])}\n" \
               f"----- {caretaker} Caretakers:\n" \
               f"{sep.join([str(el) for el in self.workers if el.__class__.__name__ == 'Caretaker'])}\n" \
               f"----- {vet} Vets:\n" \
               f"{sep.join([str(el) for el in self.workers if el.__class__.__name__ == 'Vet'])}"