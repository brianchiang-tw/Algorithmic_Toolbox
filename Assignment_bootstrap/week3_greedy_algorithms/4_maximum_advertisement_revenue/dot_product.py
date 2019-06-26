#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    

    # print("a", a)
    # print("b", b)

    # Sort vector a and vector b on descending order
    a.sort( reverse=True )
    b.sort( reverse=True )

    # print("a", a)
    # print("b", b)

    # Concept: maximum sum of product comes from each maximum product on every index
    sum_of_product = 0
    for i in range( len(a) ):
        sum_of_product += a[i] * b[i]
    return sum_of_product



# entry point of program
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print( max_dot_product(a, b) )
    
