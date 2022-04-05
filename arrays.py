from random import randint
from functools import reduce

class Array:

    def __init__(self, capacity: int, fill_value=None):
        self.capacity = capacity
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __randreplace__(self, lower_random, upper_random) -> list:
        """
        Set a random int value in range[lower_random, upper_random] and return new list.
        """
        return [self.__setitem__(i, randint(lower_random, upper_random)) for i in range(self.__len__())]
        
    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    def __sumelements__(self):
        return reduce(lambda a, b: a + b, self.items)
