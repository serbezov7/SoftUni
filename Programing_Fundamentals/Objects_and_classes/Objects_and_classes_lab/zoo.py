class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        info = ""
        if species == "mammal":
            info += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}"
        elif species == "fish":
            info += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}"
        elif species == "bird":
            info += f"Birds in {self.zoo_name}: {', '.join(self.birds)}"
        return f"{info}\nTotal animals: {Zoo.__animals}"


name_of_the_zoo = input()
zoo = Zoo(name_of_the_zoo)
number = int(input())
for animal in range(number):
    species, name = input().split()
    zoo.add_animal(species, name)
info = input()
print(zoo.get_info(info))
