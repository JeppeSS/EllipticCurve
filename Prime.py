import random
import math

def choose_k_and_q(n):
    """
    Tool for choosing n-1 = 2**k * q needed in Miller-Rabin test
    :param n: Possible prime
    :return: q -(odd integer) and k -(integer)
    """
    t = n - 1
    last_number = 0

    x = 1
    while x < n:
        try:
            if t % (2 ** x) != 0:
                break
            else:
                last_number = x
        except:
            break
        x += 1
    k = last_number
    q = t // (2 ** k)
    return k, q


def miller_rabin_test(n, a):
    """
    The Miller-Rabin test (almost as given in the book)
    :param n: Integer to be tested
    :param a: Potential witness to n
    :return: Returns true if n is (probably not) a composit number - else false
    """

    if n % 2 == 0 or 1 < math.gcd(a, n) < n:
        return False
    k, q = choose_k_and_q(n)
    a = pow(a, q, n)
    if a % n == 1:
        return True
    i = 0
    while i <= k:
        if (a % n) == 1:
            return True
        a = pow(a, 2, n)
        i += 1
        if (i % 10) == 0:
            print(i)
    return False



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


        if not self.test_if_prime(number, 100):
            raise Exception('The prime is not valid!')


    def getNumber(self):
        return self.__number__
    
    
    def test_if_prime(self, n, k):
        """
        Tests if a given value is prime
        :param n: integer to be tested
        :param k: number of times to test by Miller-Rabin test
        :return: boolean - true if n=prime - else false
        """
        
        if n == 1:
            return False

        if n == 2:
            return True


        b = False
        c = 0
        while c < k:
            c += 1
            test_val = random.randint(2, (n - 2))
            b = miller_rabin_test(n, test_val)
            if not b:
                break
        return b



    def __repr__(self):
        return '[P = %d]' % self.getNumber()



