# Uses python3
import sys
import itertools



# A variant of discrete_0_or_1_knapsack to solve 3-partition with equal sum
def discrete_0_or_1_knapsack( capacity, item_list, lookup_table):


    match_of_capacity = 0

    for y in range( 1, len(lookup_table) ):
        for current_capacity in range( 1, len(lookup_table[0]) ):

            item_i = y - 1

            
            if(  current_capacity - item_list[item_i] >= 0):
                # get the weight of picking item_i
                weight_of_picking_item_i = lookup_table[ y-1 ][ current_capacity - item_list[item_i] ] + item_list[item_i]

            else:
                # can not picking item_i because remaining space: (capacity-item_i) is negative (can not take anymore)
                weight_of_picking_item_i = 0            

            # get the weight of not picking item_i
            weight_of_not_picking_item_i = lookup_table[y-1][ current_capacity ] + 0

            max_weight = max(weight_of_picking_item_i, weight_of_not_picking_item_i)

            lookup_table[y][current_capacity] = max_weight

            if capacity == max_weight:
                # if capacity is matched, then there is a subset of summation = capacity
                match_of_capacity += 1


    if match_of_capacity >= 3:
        # There are 3 subsets with equal sum
        return 1

    else:
        # Cannoy make 3 subsets with equal sum
        return 0



# preprocessing 
def find_3_partition_of_equal_sum( target_sum, series):
    # write your code here

    # target_sum: sum value of subset of 3-partition
    # series: input sequence of numbers


    lookup_table = [ [ 0 for x in range(target_sum+1) ] for u in range( len(series)+1) ]

    existence_of_3_partition_of_equal_sum = discrete_0_or_1_knapsack( target_sum, series, lookup_table )

    # debug message
    # print_2d_array( lookup_table )

    return existence_of_3_partition_of_equal_sum



# function trigger
def partition3(A):


    sum_value = sum(A)

    if 0 != sum_value % 3 or len(A) < 3:
        # There is no perfect 3 subset of equal sum if one of those following conditions is True
        # 1. sum_value of A is not dividable by 3
        # 2. total elements number of A is smaller than 3
        return 0

    else:
        return find_3_partition_of_equal_sum( target_sum = sum_value // 3, series = A)

    

# Entry point of program
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

