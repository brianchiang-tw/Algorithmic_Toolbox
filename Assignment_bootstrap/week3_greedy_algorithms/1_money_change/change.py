# Uses python3
import sys


def sum_of_change_set( number_of_coin, coin_value):

    sum = 0
    for index in range( len(number_of_coin) ):
        sum += number_of_coin[index] * coin_value[index]

    return sum



def get_change( target_value ):
    
    coin_value = [10, 5, 1]
    number_of_coin = [0]*3

    # initialize the index of largest coin
    largest_coin_index = 0

    # initialize the remaining target value
    remaining_target_value = target_value

    while sum_of_change_set(number_of_coin, coin_value) != target_value:


        # print("sum of change set", sum_of_change_set(number_of_coin, coin_value) )
        # print("remaining_target_value", remaining_target_value )

        # change to largest coin as many as possible
        number_of_current_largest_coin = remaining_target_value // coin_value[largest_coin_index]


        # print("coin value", coin_value[largest_coin_index] )
        # print("number of coin", number_of_current_largest_coin )


        if 0 != number_of_current_largest_coin:

            # target_value is changeable by largest_coin
            # update number_of_coin
            number_of_coin[largest_coin_index] = number_of_current_largest_coin
        else:
            # target_value is NOT changeable by largest_coin
            pass


        # update remaining amount of target_value after current change in respect of largest coin
        remaining_target_value = remaining_target_value - number_of_current_largest_coin * coin_value[largest_coin_index]

        # change to second largest coin on next iteration
        largest_coin_index += 1


    return m

if __name__ == '__main__':
    m = int( input() )
    print(get_change(m))
