from arrays import Array

class Cube():

    def __init__(self, rows, columns, depth, fill_value = None):
        for i in range(rows):
            self.cube = Array(rows)
            for row in range(rows):
                self.cube[row] = Array(columns, fill_value)
                for columns in range(columns):
                    self.cube[row][columns] = Array(depth, fill_value)

    def get_height(self):
        return len(self.cube)

    def get_width(self):
        return len(self.cube[0])

    def get_depth(self):
        return len(self.cube[0][0])

    def __getitem__(self, index):
        return self.cube[index]

    def __str__(self):
        """
        Return string values from tri-dimentional array
        """
        result = ""

        for row in range(self.get_height()):
            for column in range(self.get_width()):
                for depth in range(self.get_depth()):
                    result += str(self.data[row][column][depth]) + " "
            
            result += "\n"
        
        return str(result)
        