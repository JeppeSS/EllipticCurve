class EllipticCurve(object):
    
    __a__ = None
    __b__ = None

    def __init__(self, a, b):
        self.__a__ = a
        self.__b__ = b

        if not self.satisfyCurve(self.__a__, self.__b__):
            raise Exception('The curve is not valid!')


    def satisfyCurve(self, a, b):
        discri = -16 * (((4 * self.__a__) ** 3) + ((27 * self.__b__) ** 2))

        return discri != 0
        
