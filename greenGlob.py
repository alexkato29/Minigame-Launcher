from random import randint

class GreenGlob (object):
    def __init__(self, width, height):
        self.xCoord = self.genXCoord(width)
        self.yCoord = self.genYCoord(height)

    def __str__(self):
        return "(" + str(self.xCoord) + ", " + str(self.yCoord) + ")"

    def genXCoord(self, width):
        return randint(15, width - 15)

    def genYCoord(self, height):
        return randint(15, height - 15)

    __repr__ = __str__