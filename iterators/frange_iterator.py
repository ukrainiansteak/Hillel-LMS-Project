class FRangeIterator:
    def __init__(self, start, end, step):
        self.element = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.element >= self.end:
            raise StopIteration()
        if self.element % 1 == 0:
            result = round(self.element)
        else:
            result = self.element
        self.element += self.step
        return result


for i in FRangeIterator(0, 100, 2.5):
    print(i)
