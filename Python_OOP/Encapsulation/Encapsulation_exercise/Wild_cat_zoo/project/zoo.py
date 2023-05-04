from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []  # Animal objects
        self.workers = []  # Worker objects

    def add_animal(self, animal: Animal, price):
        if price > self.__budget:
            return "Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        costs = sum(w.salary for w in self.workers)
        if costs > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= costs
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        costs = sum(a.money_for_care for a in self.animals)
        if costs > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= costs
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = ""
        result += f"You have {len(self.animals)} animals\n"

        lions = [str(a) for a in self.animals if isinstance(a, Lion)]
        tigers = [str(a) for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [str(a) for a in self.animals if isinstance(a, Cheetah)]

        result += f"----- {len(lions)} Lions:\n" + '\n'.join(lions) + "\n"
        result += f"----- {len(tigers)} Tigers:\n" + '\n'.join(tigers) + "\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n" + '\n'.join(cheetahs)

        return result

    def workers_status(self):
        result = ""
        result += f"You have {len(self.workers)} workers\n"

        keepers = [str(a) for a in self.workers if isinstance(a, Keeper)]
        caretakers = [str(a) for a in self.workers if isinstance(a, Caretaker)]
        vets = [str(a) for a in self.workers if isinstance(a, Vet)]

        result += f"----- {len(keepers)} Keepers:\n" + '\n'.join(keepers) + "\n"
        result += f"----- {len(caretakers)} Caretakers:\n" + '\n'.join(caretakers) + "\n"
        result += f"----- {len(vets)} Vets:\n" + '\n'.join(vets)

        return result















