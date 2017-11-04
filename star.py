from circle import Circle
from point import Point
import random

class Star(Circle):
    def __init__(self):
        super().__init__(random.randrange(0, 640, 5),random.randrange(0, 480, 5), 1,0 )






