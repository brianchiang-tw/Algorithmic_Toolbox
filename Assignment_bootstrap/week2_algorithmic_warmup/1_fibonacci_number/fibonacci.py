# Uses python3
def calc_fib(n):

    if n >= 2:
        # Inductive step
        # Fib( n ) = Fib( n-1 ) + Fib( n-2 ) for n >= 2
        fib_func_value = [0]*(n+1)
    
        fib_func_value[0] = 0 
        fib_func_value[1] = 1

        for index in range(2, (n+1) ):
            fib_func_value[ index ] = fib_func_value[ index-1 ] + fib_func_value[ index-2 ]

        return fib_func_value[n]

    else:
        # Base case:
        # Fib( 0 ) = 0, for n = 0
        # Fib( 1 ) = 1, for n = 1
        return n


    
n = int(input())
print( calc_fib(n) )
