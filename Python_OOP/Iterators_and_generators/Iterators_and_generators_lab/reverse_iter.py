class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):

        index = self.index - 1
        if index >= 0:
            self.index -= 1
            return self.iterable[index]
        else:
            raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
