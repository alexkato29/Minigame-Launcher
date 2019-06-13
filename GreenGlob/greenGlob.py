from GreenGlob import Coordinate as c
from random import randint

class GreenGlob (object):
    def __init__(self, width, height):
        self.coord = c.Coordinate(self.genXCoord(width), self.genYCoord(height))
        self.xCoord = self.coord.x
        self.yCoord = self.coord.y

    def __repr__(self):
        return "(" + str(self.xCoord) + ", " + str(self.yCoord) + ")"

    def genXCoord(self, width):
        return randint(15, width - 15)

    def genYCoord(self, height):
        return randint(15, height - 15)