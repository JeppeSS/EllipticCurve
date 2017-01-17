class EllipticCurve(object):
    
    __a__     = None
    __b__     = None
    __prime__ = None

    def __init__(self, a, b, prime):
        self.__a__     = a
        self.__b__     = b
        self.__prime__ = prime


        if not self.satisfyCurve(self.__a__, self.__b__):
            raise Exception('The curve is not valid!')

    def geta(self):
        return self.__a__

    def getb(self):
        return self.__b__

    def getPrime(self):
        return self.__prime__

    def satisfyCurve(self, a, b):
        """ SatisfyCurve is a check that needs to be done to exclude singular
            curves.

            4a^3 + 27b^2 ≠ 0

        """
        discri = -16 * (((4 * self.geta()) ** 3) + ((27 * self.getb()) ** 2))

        return discri != 0



    def __repr__(self):
        return '[y^2 = x^3 + %dx + %d mod %d]]' % (self.geta(), self.getb()
                                                 , self.getPrime())

