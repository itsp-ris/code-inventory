'''
ID: 28390121
author: Priscilla Tham
Date: 07/06/2020
'''
import argparse as ap
import random
import math


def repeatedSquaring(base, exp, mod, res):
    '''
    function performs modular exponentiation by repeated squaring
    precondition:
    :param base: the base value
           exp: the exponent
           mod: the modular value
           res: array storing consecutive modular exponentiation result
    postcondition:
    :return: the array storing consecutive modular exponentiation result
    complexity: time: best and worst: O(m) where m is the exponent
                space: O(m) where m is the exponent
    error handling:
    '''
    # base case
    if exp == 0:
        res += [int(base % mod)]
        return res
    # recursive case
    else:
        repeatedSquaring(base, exp - 1, mod, res)
        res += [int(res[-1] * res[-1] % mod)]
        return res


def MillerRabinRandomizedPrimality(n, k):
    '''
    function tests primality of a number using the Miller Rabin algorithm
    precondition: number tested for primality is > 2
    :param n: number tested for primality
           k: the number of bits representing n
    postcondition:
    :return: boolean indicating whether n is definitely not prime or maybe prime
             a) 0: Definitely not prime and
             b) 1: Maybe prime
    complexity: time: best and worst: O(k log n) where k is the number of bits representing n and n is the number
                                      tested for primality
                space: O(m) where m is the exponent
    error handling:
    '''
    determinant = 2
    if n % determinant == 0:
        return 1

    s = 0
    t = n - 1
    # O(log n)
    while t % determinant == 0:
        s = s + 1
        t = t//2

    res = None
    # O(k)
    for _ in range(k):
        a = random.randint(2, n - 2)
        if int(math.pow(a, n - 1) % n) != 1:
            return 1
        # O(m)
        if res is None:
            res = repeatedSquaring(a, s*t, n, [])
        # (log n)
        for i in range(1, s + 1):
            if res[i] == 1 and (res[i - 1] != 1 or res[i - 1] != -1):
                return 1
    return 0


def genPrime(k):
    '''
    function generates random prime by incorporating the Miller Rabin algorithm
    precondition: the number of bits representing the prime must be >= 64 bits, otherwise, cap to 64
    :param k: the number of bits representing the prime number
    postcondition:
    :return: n: the number tested as maybe prime using Miller Rabin algorithm, otherwise, "Not found"
    complexity: time: best and worst: O(k log n) where k is the number of bits representing n and n is the number
                                      tested for primality
                space: O(m) where m is the exponent
    error handling:
    '''
    mn = int(math.pow(2, k-1))
    mx = int(math.pow(2, k) - 1)
    end = max(64, int(mx/math.log(mx) - mn/math.log(mn)))

    for _ in range(end):
        n = random.randint(mn, mx)
        # O(k log n)
        if MillerRabinRandomizedPrimality(n, k) == 0:
            return n
    return "Not found"


def main():
    # create a parser object
    parser = ap.ArgumentParser()

    # specify what arguments will be coming from the terminal/commandline
    parser.add_argument("k", help="specifies an integer", type=int)

    # get all the arguments
    arguments = parser.parse_args()

    # Extract the required arguments
    k = arguments.k

    while True:
        try:
            print(genPrime(k))
        except ValueError:
            return


if __name__ == '__main__':
    main()

