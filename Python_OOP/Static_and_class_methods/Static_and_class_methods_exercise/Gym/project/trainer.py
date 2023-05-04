from project.mixin import MyMixin


class Trainer(MyMixin):
    ID = 0

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
