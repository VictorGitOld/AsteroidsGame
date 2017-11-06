from polygon import Polygon
from point import Point
from math import cos,sin,pi
import random

class Rocks(Polygon):
    #Each time rock is called it creates a rock object of random 1-3 sizes and then divides a circle in a random amount
    #of pies between 9 and 24. from origo(0,0) a point is created at random 30-50 length inbetween each piece of pie
    #creating more random rocks. also Pull is dependent on level, but in future the level variable might be moved from
    #the rock class.
    def __init__(self,level):
        self.level = level

    #send all rocks to polygon class.
        super().__init__(
            self.getRock(),
            x=random.randint(0, 640),
            y=random.randint(0, 480),
            rotation=random.randrange(0, 50, 5),
            pull=Point(round(random.uniform(0, 0.5), 1)*self.level*2, round(random.uniform(0, 0.5), 1)*self.level*2),
            angular_velocity=round(random.uniform(-0.5, 0.5), 1))

    def getRock(self):
        randomSize = random.randint(1,3)
        pointList=[]
        randomNrOfSplits=random.randint(9,24)
        radiusSplits=360/randomNrOfSplits

        for currentSplit in range(randomNrOfSplits):
            aggregatedRadius = radiusSplits * currentSplit + radiusSplits
            length=random.randint(30,50)/randomSize
            xNew=cos(aggregatedRadius*pi/180)*length
            yNew=sin(aggregatedRadius*pi/180)*length
            pointList.append(Point(xNew,yNew))
        return pointList