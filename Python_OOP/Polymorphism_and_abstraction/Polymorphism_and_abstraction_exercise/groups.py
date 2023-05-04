class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people  # Person objects

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __str__(self):
        names = [str(p) for p in self.people]
        return f"Group {self.name} with members {', '.join(names)}"

    def __getitem__(self, idx):
        return f"Person {idx}: {self.people[idx]}"

