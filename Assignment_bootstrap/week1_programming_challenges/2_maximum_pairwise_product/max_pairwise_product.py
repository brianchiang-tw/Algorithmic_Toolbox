# python3

def get_max_and_remove_max( numbers ):

    # Find and pick the maximum value
    max_value = max( numbers )

    # Remove the maximum value in numbers
    numbers.remove( max_value )

    return max_value


def max_pairwise_product( numbers ):


    max_value_1st = get_max_and_remove_max( numbers )
    max_value_2nd = get_max_and_remove_max( numbers )

    max_product = max_value_1st * max_value_2nd

    return max_product


if __name__ == '__main__':

    # get the total number of input
    input_n = int( input() )

    # get the number series of input
    input_numbers = [int(x) for x in input().split()]

    print( max_pairwise_product(input_numbers) )
