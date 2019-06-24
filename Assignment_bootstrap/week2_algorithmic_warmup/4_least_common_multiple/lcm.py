# Uses python3
import sys


def gcd_euclidean(a, b):
    
    if a < b:
        # Always keep the larger one on the first place, smaller one on the second place.
        a, b = b, a


    # Base case:
    # GCD( a, b ) = a , if b == 0

    # Inductive step:
    # GCD( a, b ) = GCD( b, r ) where r = a % b, the remainder of a / b
    
    while b != 0:

        remainder = a % b
        a = b
        b = remainder

    return a



def lcm_euclidean(a, b):

    # proof:

    # Assume a, b as following
    # a = gcd * s
    # b = gcd * t

    # a * b = gcd * s * gcd * t
    # a * b = gcd * gcd * s * t
    # a * b = gcd * ( gcd * s * t )
    # a * b = gcd * lcm

    # Finally, we get the formula
    # lcm = a * b / gcd 

    # // means integer division
    least_common_multiple = ( a * b ) // gcd_euclidean( a, b )

    return least_common_multiple

if __name__ == '__main__':

    a, b = map(int, input().split())
    print(lcm_euclidean(a, b))

