class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.number = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == self.count:
            raise StopIteration

        self.number += 1

        return self.count - self.number


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")