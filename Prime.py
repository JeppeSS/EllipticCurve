class Prime(object):
    __number__ = None 

    def __init__(self, number):
        self.__number__ = number

    def getNumber(self):
        return self.__number__

    def __repr__(self):
        return '[P = %d]' % self.getNumber()

