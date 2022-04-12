from arrays import Array

class Stack():
    def __init__(self, limit):
        self.top = None
        self.size = 0
        self.limit = self.set_limit(limit)
        self.array = self.set_array()
        
        
    def push(self, data):
        """
        add an element to the top of the stack
        """
        # Create an var to get last element in stack
        aux = self.size
        if aux >= self.limit:
            raise IndexError
        else:
            self.array[aux] = data
        self.size += 1

    def pop(self):
        """
        Remove top element of the list
        """
        if self.size <= 0:
            self.size -= 1

            aux = self.size
            data = self.array[aux]
            self.array[aux] = None
            
            self.top = self.array[aux - 1]
            return data
        else:
            return "there no elements in stack"


    def __iter__(self):
        """
        Return an iterable
        """
        return self.array.__iter__()

    def __str__(self):
        """
        Return a string
        """
        return self.array.__str__()

    def length(self):
        """
        Return size of the stack
        """
        return self.size

    def search(self, data):
        count = 0
        for i in self.__iter__():
            if i == data:
                return (True, count)
            count + 1
        return False

    def get_array(self):
        return self.array

    def set_array(self):
        array = Array(self.limit)

        return array

    def get_limit(self):
        return self.limit

    def set_limit(self, limit):
        return limit