"""
nice guide for implementation:
https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Primality_Testing

page 127 in crypto-book also usefull
"""

import fractions
import random


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
    if n % 2 == 0 or 1 < fractions.gcd(a, n) < n:
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

def test_if_prime(n, k):
    """
    Tests if a given value is prime
    :param n: integer to be tested
    :param k: number of times to test by Miller-Rabin test
    :return: boolean - true if n=prime - else false
    """
    b = False
    c = 0
    while c < k:
        c += 1
        test_val = random.randint(2, (n - 2))
        b = miller_rabin_test(n, test_val)
        if not b:
            break
    return b

def generate_prime(lower_range, upper_range, k):
    """
    Returns a prime in a given range - the function will never return if no
    primes is in the given range
    :param lower_range: the minimum values of the new prime
    :param upper_range: The maximum value of the new prime
    :param k: The number of times a potential prime is tested by Miller-Rabin
    :return: A prime number (most likely)
    """
    b = False
    test_val = -1
    while not b:
        test_val = random.randint(lower_range, upper_range)
        b = test_if_prime(test_val, k)
    if test_val < 0:
        raise
    return test_val


"""
Test:

The value of test_p are confirmed primes

test_p = [696976764637, 20615192584997, 2500150826461, 1389959373163]

for p in test_p:
    assert test_if_prime(p, 1000)

The value of test_not_p are confirmed composite numbers

test_not_p = [696976764636, 20615192584998, 2501130826460, 1389999379162]

for n_p in test_not_p:
    assert not test_if_prime(n_p, 1000)
"""