from Ch4Array_and_Linked.arrays import Arrays

class Grid:
    """用Arrays实现二维数组"""
    def __init__(self,rows,columns,fillValue = None):
        self.data = Arrays(rows)
        for i in range(rows):
            self.data[rows] = Arrays(columns,fillValue)

    def getHeight(self):
        return len(self.data)

    def getWidth(self):
        return len(self.data[0])

    def __getitem__(self, item):
        return self.data[item]

    def __str__(self):
        result = ""
        for row in range(self.getHeight()):
            for col in range(self.getHeight()):
                result += str(self.data[row][col]) + ""
            result += "\n"
        return result
    







