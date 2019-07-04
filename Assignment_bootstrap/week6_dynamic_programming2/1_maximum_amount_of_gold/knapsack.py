# Uses python3
import sys
import os



def print_2d_array( image_matrix, mode = "Hex" ):

    image_height = len( image_matrix )


    image_width = len( image_matrix[0] )


    for y in range( image_height ):
        for x in range( image_width ):

            if "Hex" == mode:
                print( "{:02X}".format( image_matrix[y][x] ), end = ' ' )
            elif "Decimal" == mode:
                print( "{: 10d}".format( image_matrix[y][x] ), end = ' ' )
            else:
                print("Invliad print mode  {:<10} is not supported.".format(mode) )

        print()    

    # One more extra new line in order to keep output neat and tidy
    print("\n")



def discrete_0_or_1_knapsack( capacity, item_list, lookup_table):

    if not item_list or capacity < 0:
        # item_list is empty, max weight = 0
        # capacity is negative(cannot take item anymore), max weight = 0
        return 0

    else:

        if 0 != lookup_table[len(item_list)][capacity]:
            # early return if lookup table has result of maximal weight on sub-problem
            return lookup_table[len(item_list)][capacity]

        else:



            # remove and return last item (i.e., item_i)
            item_i = item_list[-1]

            # weight_of_picking_item_i = 0
            if(  capacity-item_i >= 0):
                # get the weight of picking item_i
                weight_of_picking_item_i = discrete_0_or_1_knapsack( capacity-item_i, item_list[0:-1], lookup_table) + item_i

            else:
                # can not picking item_i because remaining space: (capacity-item_i) is negative (can not take anymore)
                weight_of_picking_item_i = 0


            # get the weight of not picking item_i
            weight_of_not_picking_item_i = discrete_0_or_1_knapsack( capacity, item_list[0:-1], lookup_table) + 0

            # pick maximal weight
            max_weight = max(weight_of_picking_item_i, weight_of_not_picking_item_i)

            # update lookup table
            lookup_table[len(item_list)][capacity] = max_weight

            return max_weight



def optimal_weight(W, w):
    # write your code here

    # W: Max capacity of bag
    # w: list of gold with weight_#i


    lookup_table = [ [ 0 for x in range(W+1) ] for u in range( len(w)+1) ]

    max_weight = discrete_0_or_1_knapsack( W, w, lookup_table )

    # debug message
    # print_2d_array( lookup_table )

    return max_weight

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
