def xgcd(j, p):
    """
    Extended Euclidean algorithm
    implemented as Iterative algorithm to optimize speed.
    

    Code source: https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
    """
    x0, x1, y0, y1 = 1, 0, 0, 1

    while p != 0:
        q, j, p = j // p, p, j % p
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return j, x0, y0

class Point(object):
    """
    Point object

    If x == 0 and y == 0, the point represents infinity
    If the point is does not exists in the finite field raise exception
    """
    __x__  = None
    __y__  = None

    __EC__ = None


    def __init__(self, curve, x, y):
        self.__x__  = x
        self.__y__  = y
        
        self.__EC__ = curve
        if x != 0 and y != 0:        
            if not self.__EC__.pointTest(self.__x__, self.__y__):
                raise Exception('The point is not valid!')


    def getX(self):
        return self.__x__

    def getY(self):
        return self.__y__

    def getCoords(self):
        return (self.getX(), self.getY())
    
    def getCurve(self):
        return self.__EC__

    def setX(self, x):
        self.__x__ = x

    def setY(self, y):
        self.__y__ = y

    def setCoords(self, x, y):
        self.__x__ = x
        self.__y__ = y

    def __eq__(self, Q):
        """
        Test if two points are equal
        """
        return (self.getX(), self.getY()) == (Q.getX(), Q.getY())

    def __inv__(self):
        """
        Takes the inverse of a point

        (x, y) = (x, -y)
        """
        
        curve = self.getCurve()
        prime = curve.getPrime()

        x    = self.getX()
        y    = self.getY()
        newY = (-y) % prime 

        return Point(curve, x, newY) 

    def div(self, i, j, p):
        """
        Division with modular arithmetic
        """
        e = xgcd(j, p)
        d = i * e[1]

        return d % p

    def add(self, Q):
        """
        Point addion, following the addion laws. 
        If P == Q, then do point doubling insted.
        returns a new point inside the finite field.
        """
        if self.__eq__(Q):
            return self.double()

        if self.getX() == 0 and self.getY() == 0:
            return Q

        if Q.getX() == 0 and Q.getY() == 0:
            return self

        if self.getX() == Q.getX():
            raise Exception('If x1 == x2 the point does not exist')

        curve = self.getCurve()
        prime = curve.getPrime()

        sY = (self.getY() - Q.getY()) % prime
        sX = (self.getX() - Q.getX()) % prime

        s = self.div(sY, sX, prime)

        rX = ((s ** 2) - self.getX() - Q.getX()) % prime
        rY = (s * (self.getX() - rX) - self.getY()) % prime

        return Point(curve, rX, rY)



    def double(self):
        """
        Point doubling. 
        returns a new point in the finite field.
        """
        curve = self.__EC__
        prime = curve.getPrime()
        a     = curve.geta()


        sX = (3 * (self.getX() ** 2) + a)
        sY = (2 * self.getY())

        s = self.div(sX, sY, prime)


        rX = ((s ** 2) - (2 * self.getX())) % prime
        rY = (s * (self.getX() - rX) - self.getY()) % prime


        return Point(curve, rX, rY)


    def double_and_add(self, n):
        """
        The discrete logarithm problem. Double_and_add,
        doubles the point n times.

        Uses n//2 to work with arbitary large integers.

        returns a new point in the finite field.
        """
        Q = self
        R = Point(self.__EC__, 0, 0)

        while n > 0:

            if n % 2 == 1:
                R = R.add(Q)

            Q = Q.double()
            n = int(n // 2)


        return R

    def __repr__(self):
        return '[x = %d, y = %d]' % (self.getX(), self.getY())

