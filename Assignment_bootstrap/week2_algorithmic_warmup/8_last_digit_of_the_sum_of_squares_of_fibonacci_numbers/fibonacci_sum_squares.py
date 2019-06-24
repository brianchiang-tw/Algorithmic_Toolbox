# Uses python3
from sys import stdin

# Return a table of Fib(n, m) for fibonacci series modulo m
def get_table_of_fibonacci_modulo_m_(n, m):



    ## Early return on base case
    if n <= 1:

        fib_func_array = [0] * 2
        fib_func_array[0] = 0 % m
        fib_func_array[1] = 1 % m


        return (fib_func_array, 2)



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
    # equvilent_term = n % period_of_fib_mod_m

    # Get the Fib(n, m) by look-up table over fib_func_array
    # fib_n_of_module_m = fib_func_array[equvilent_term]


    return fib_func_array, period_of_fib_mod_m



# return the square sum of last digits of fibonacci series
def fibonacci_square_sum_last_digit_partial( end ):

    n = end
    n_plus_1 = end + 1

    fib_func_array, period_of_fib_mod_m = get_table_of_fibonacci_modulo_m_( n_plus_1, m = 10)

    # F0^2 + F1%2 + ... + Fn^2 = Fn * Fn+1

    fib_n = fib_func_array[ n % period_of_fib_mod_m ]
    fib_n_1 = fib_func_array[ n_plus_1 % period_of_fib_mod_m ]

    square_sum = fib_n * fib_n_1

    last_digit = square_sum % 10

    return last_digit



if __name__ == '__main__':
    n = int( input() )
    print( fibonacci_square_sum_last_digit_partial(n) )
