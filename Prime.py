class Prime(object):
    """
    Prime object, represents prime numbers.
    Used to check if number actually is prime.

    """

    __number__ = None 

    def __init__(self, number):
        """
        Initialize a "prime" number, the objects does not automaticlly check
        if the number is actually prime.

        Args:
            number (int): A prime number
        """
        self.__number__ = number


    def getNumber(self):
        return self.__number__

    def __repr__(self):
        return '[P = %d]' % self.getNumber()

