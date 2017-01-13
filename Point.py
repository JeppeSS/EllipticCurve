class Point(object):
    __x__ = None
    __y__ = None


    def __init__(self, x, y):
        self.__x__ = x
        self.__y__ = y


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

