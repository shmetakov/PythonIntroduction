class Worker:
    name = None
    surname = None

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


worker_1 = Position("Иван", "Петров", "Водитель", 20000, 5000)
print(worker_1.get_full_name())
print(worker_1.get_total_income())
print()
print(worker_1.name)
print(worker_1.surname)
print(worker_1.position)