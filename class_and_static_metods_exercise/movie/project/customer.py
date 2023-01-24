class Customer:
    def __init__(self, name, age, costumer_id):
        self.name = name
        self.age = age
        self.id = costumer_id
        self.rented_dvds = []

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} " \
            f"rented DVD's ({', '.join(m.name for m in self.rented_dvds)})"

