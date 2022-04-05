from arrays import Array

class Cube():

    def __init__(self, rows, columns, depth, fill_value = None):
        """
        Create tri-dimentional Arrays
        Giving numbers of rows, columns and depth to get an Array
        """
        self.cube = [Array(columns, Array(depth)) for i in range(rows)]

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
                    result += str(self.cube[row][column][depth]) + " "
            
            result += "\n"
        
        return str(result)
        