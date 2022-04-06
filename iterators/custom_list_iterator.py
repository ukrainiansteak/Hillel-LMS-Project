class CustomListIterator:
    def __init__(self, collection):
        self.collection = collection
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            print(f"Try element at position {self.position}")
            result = self.collection.data[self.position]
            self.position += 1
            print(f"Advance to position {self.position}")
            return result
        except IndexError:
            print(f"Stop Iteration. No Element on position {self.position}")
            raise StopIteration()


class CustomList:
    def __init__(self, from_list=None):
        self.data = from_list and list(from_list) or []

    def __iter__(self):
        print("Get Custom List Iterator")
        return CustomListIterator(self)


class RoundedListIterator:
    def __init__(self, some_collection):
        if not some_collection:
            raise ValueError("Collection is empty")

        self.collection = some_collection
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position == len(self.collection):
            self.position = 0

        result = self.collection[self.position]
        self.position += 1
        return result


lst = [1, 2, 3, 4, 5, 6]
round_iterator = RoundedListIterator(lst)

for i in range(20):
    print(next(round_iterator))
