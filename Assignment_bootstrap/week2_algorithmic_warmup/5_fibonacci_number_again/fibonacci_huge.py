# Uses python3
import sys

def get_fibonacci_modulo_m_(n, m):

    # Early return on base case
    if n <= 1:
        return n % m



    maximum_period = m**2
    array_size = maximum_period + 1

    # Create a array to store the value of Fibonacci modulo m
    fib_func_array = [0] * (array_size)

    # Base case
    fib_func_array[0] = 0 % m
    fib_func_array[1] = 1 % m

    # Update table, fib_func_array, with respect to modulo m
    for index in range(2, array_size):
        # Inductive step:
        fib_func_array[index] = ( fib_func_array[index-1] + fib_func_array[index-2] ) % m
        # print("fib_func_array[{}] = {} ".format( index, fib_func_array[index] ) )


    # Find period of fun_func_array
    for index in range(2, array_size):
        # print("fib_func_array[{}] = {} ".format( index, fib_func_array[index] ) )
        if fib_func_array[index] == 0 and fib_func_array[index+1] == 1:
            period_of_fib_mod_m = index
            break

    # print("period: {}".format(period_of_fib_mod_m) )

    # Calculate the equvilent term to n, due to the cyclic periodic property of fibonacci value modulo m
    equvilent_term = n % period_of_fib_mod_m

    # Get the Fib(n, m) by look-up table over fib_func_array
    fib_n_of_module_m = fib_func_array[equvilent_term]


    return fib_n_of_module_m

if __name__ == '__main__':

    n, m = map(int, input().split())
    print( get_fibonacci_modulo_m_(n, m) )
