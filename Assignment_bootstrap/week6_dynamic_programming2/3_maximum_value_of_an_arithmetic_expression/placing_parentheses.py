# Uses python3
import math



# evaluate a op b
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False



# get min and max value of expression[i,j]
def min_and_max( max_val_array, min_val_array, i, j, operator_arr ):

    # initialization of min_value as well as max_value
    min_value = math.inf
    max_value = -math.inf
    
    for k in range(i,j):

        # calculate all four possible candidates
        candidate_1 = evalt( max_val_array[i][k], max_val_array[k+1][j], operator_arr[k] )
        candidate_2 = evalt( max_val_array[i][k], min_val_array[k+1][j], operator_arr[k] )
        candidate_3 = evalt( min_val_array[i][k], max_val_array[k+1][j], operator_arr[k] )
        candidate_4 = evalt( min_val_array[i][k], min_val_array[k+1][j], operator_arr[k] )

        # update min and max value on each iteration of index k
        min_value = min( min_value, candidate_1, candidate_2, candidate_3, candidate_4 )
        max_value = max( max_value, candidate_1, candidate_2, candidate_3, candidate_4 )


    return min_value, max_value



# function trigger
def get_maximum_value(dataset):
    #write your code here

    # initialization of operators and operands to empty list
    operators = []
    operands = []

    for element in dataset:

        if element in ['+','-','*']:
            operators.append( element )

        else:
            operands.append( int(element) )


    size = len(operands)

    min_value_array = [ [ 0 for x in range(size) ] for y in range(size) ]
    max_value_array = [ [ 0 for x in range(size) ] for y in range(size) ]

    # initialization of diagnal element of min value array as well as max value array
    for index in range( size ):
        min_value_array[index][index] = operands[index]
        max_value_array[index][index] = operands[index]


    # calculate and update min value array and max value array by zig-zag scan
    for delta in range(1,size):
        for i in range(0, size-delta):

            j = i + delta
            min_value_array[i][j], max_value_array[i][j] = min_and_max(max_value_array, min_value_array, i, j, operators)



    return max_value_array[0][size-1]



# Entry point of program
if __name__ == "__main__":
    print(get_maximum_value(input()))
