from arrays import Array

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

    def __str__(self):
        result = ""

        for row in range(self.get_height()):
            for column in range(self.get_width()):
                result += str(self.data[row][column]) + " "
            
            result += "\n"
        
        return str(result)