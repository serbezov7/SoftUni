class MyMixin:
    @classmethod
    def get_next_id(cls):
        cls.ID += 1
        return cls.ID