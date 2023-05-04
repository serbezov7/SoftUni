from project.mixin import MyMixin


class Customer(MyMixin):
    ID = 0

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

