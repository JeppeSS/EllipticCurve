import random


def gcd(x, y):
    """ Greatest common divisor, the Euclidean Algorithm 
    
    Uses while loop insted of recursion to optimize speed.
    Python works slow with recursion.


    Args:
        x (int): Positive integer
        y (int): Positive integer, x >= y
    """


    if (x <= 0) or (y <= 0):
        raise Exception('Arguments must be positive')


    while y != 0:
        x, y = y, x % y

    return x


def fermat(a, p):
    """ Fermat's little theorem

    If p is a prime number, then for any integer a:

    a ** (p - 1) ≡ 1 mod p

    This is not always the case!


    Args:
        a (int): Number to test
        p (int): The prime number you want to test 
    """

    return pow(a, p - 1, p)


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




    def isPrime(self, numTest=50):
        p = self.__number__

        if p == 1:
            return False

        if numTest >= p:
            numTest = p - 1


        for i in range(numTest):
            test = random.randint(1, p - 1)
           
            if (gcd(test, p) != 1):
                return False

            print(fermat(test, p))
            if fermat(test, p) != 1:
                return False

        return True


    def __repr__(self):
        return '[P = %d]' % self.getNumber()
