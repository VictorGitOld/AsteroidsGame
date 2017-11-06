from polygon import Polygon
from point import Point


class Ship(Polygon):
    def __init__(self, x = 1000, y = 950, rotation = 5000):

        super().__init__(x, y, rotation)
