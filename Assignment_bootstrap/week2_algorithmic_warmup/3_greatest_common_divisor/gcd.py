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



if __name__ == "__main__":
    
    a, b = map(int, input().split() )
    # print(a, b)
    print( gcd_euclidean(a, b) )
