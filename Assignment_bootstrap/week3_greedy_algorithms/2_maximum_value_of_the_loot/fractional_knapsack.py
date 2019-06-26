# Uses python3
import sys

def get_optimal_value(capacity, weights, values):

    # initialize value of pick
    value = 0.

    # get total number of item
    number_of_items = len(weights)

    # make a item pair by corresponding values and weights
    item_pair = list( zip(values, weights) )


    # Sort by value per unit weight, on descending order
    # item[0]: total value
    # item[0]: total weight
    item_pair = sorted( item_pair, key = lambda item: (item[0]/item[1]), reverse = True )
    


    # initialize the weight of pick
    weight_of_pick = [0] * number_of_items

    # initialize the remaining capacity
    remaining_capacity = capacity

    # initialize the index 
    index = 0



    while sum(weight_of_pick) != capacity:

        # max load = min of { the weight of most worthy item, remaining capacity }
        maximam_load_of_most_worthy_item = min( item_pair[index][1], remaining_capacity )

        # update weight of pick on most worthy item
        weight_of_pick[index] = maximam_load_of_most_worthy_item

        # update remaining capacity
        remaining_capacity = remaining_capacity - weight_of_pick[index]

        # value per unit weight of item
        value_per_unit_weight = item_pair[index][0]/item_pair[index][1]

        # update value of pick
        value = value + weight_of_pick[index] * value_per_unit_weight

        # pick the second worthy item on next iteration
        index += 1

    return value



# Entry point of program
if __name__ == "__main__":
    data = list( map(int, sys.stdin.read().split() ) )
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
