class FibonacciIterator:
    def __init__(self):
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result


for index, item in enumerate(FibonacciIterator(), start=1):
    if index > 10:
        break
    print(index, item)
