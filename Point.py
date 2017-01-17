import EllipticCurve as EC
import Prime as pri

class Point(object):
    __x__  = None
    __y__  = None

    __EC__ = None


    def __init__(self, curve, x, y):
        self.__x__  = x
        self.__y__  = y
        
        self.__EC__ = curve


        if not self.__EC__.pointTest(self.__x__, self.__y__):
            raise Exception('The point is not valid!')


    def getX(self):
        return self.__x__

    def getY(self):
        return self.__y__
    
    def getCoords(self):
        return (self.getX(), self.getY())

    def setX(self, x):
        self.__x__ = x

    def setY(self, y):
        self.__y__ = y

    def setCoords(self, x, y):
        self.__x__ = x
        self.__y__ = y


    def __repr__(self):
        return '[x = %d, y = %d]' % (self.getX(), self.getY())
