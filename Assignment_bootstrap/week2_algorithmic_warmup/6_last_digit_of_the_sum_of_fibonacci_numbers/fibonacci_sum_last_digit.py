# Uses python3
import sys



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



# Return of last digit of sum of fibonacci series
def fibonacci_sum_last_digit(n):

    ## Early return on base case:

    # for n = 0, ( 0 ) % 10  = 0
    # for n = 1, ( 0 + 1 ) % 10 = 1
    if n <= 1:
        return n

    fib_func_array, period_of_fib_mod_m = get_table_of_fibonacci_modulo_m_(n, m = 10)

    ## speed up for large n
    cyclic_group_sum = 0
    for index in range( period_of_fib_mod_m ):
        cyclic_group_sum += fib_func_array[ index ]

    last_digit_of_cgs = cyclic_group_sum % 10

    
    number_of_cyclic_group = n // period_of_fib_mod_m
    number_of_remaining_term = n % period_of_fib_mod_m

    # (a) Calculate last digit of total cyclic group sum
    last_digit_of_total_cgs = ( last_digit_of_cgs * number_of_cyclic_group ) % 10
    

    last_digit_sum_of_remainings = 0
    # (b) Sum up remaining terms
    for index in range(0, number_of_remaining_term+1 ):
        last_digit_sum_of_remainings = ( last_digit_sum_of_remainings + fib_func_array[ index ] ) % 10


    # get the last digit of (a) + (b)
    last_digit = ( last_digit_of_total_cgs + last_digit_sum_of_remainings ) % 10


    return last_digit



# Entry point of program
if __name__ == '__main__':

    n = int(input() )
    print( fibonacci_sum_last_digit(n) )
