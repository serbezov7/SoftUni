from project.mixin import MyMixin


class Equipment(MyMixin):
    ID = 0

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
