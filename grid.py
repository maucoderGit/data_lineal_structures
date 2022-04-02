from arrays import Array
from random import randint

class Grid():
    def __init__(self, rows, colums, fill_value= None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(colums, fill_value)

    def get_height(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, row, column, value):
        self.data[row][column] = value

    def __setRandints__(self):
        for i in range(self.get_height()):
            self.data[i] = [randint(0, self.get_width()) for i in range(self.get_width())]                

    def __str__(self):
        result = ""

        for row in range(self.get_height()):
            for column in range(self.get_width()):
                result += str(self.data[row][column]) + " "
            
            result += "\n"
        
        return str(result)