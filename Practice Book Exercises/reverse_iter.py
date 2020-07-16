class reverse_iter:
    def __init__(self, list):
        self.i = len(list) - 1
        self.list = list

    def __iter__(self):
        return reverse_iter(self.list)

    def reverse_iter(self, list):
        self.list = list

    def next(self):
        if self.i >= 0:
            i = self.i
            self.i -= 1
            return self.list[i]
        else:
            raise StopIteration()
