# Uses python3
import sys

def merge(a, b, left, mid, right):

    # Generate a sub array from left half
    array_left = list( b[ left : mid+1 ] )

    # Generate a sub array from right half
    array_right = list( b[ mid+1 : right+1 ] )


    # counter of inversion
    count_of_inversion = 0



    # Make INT_MAX, which is larger or equal to any integer, 
    # as a guard on the tail in the case that index meets the end of array_left or array_right.
    sentry_max_int = sys.maxsize
    array_left.append( sentry_max_int )
    array_right.append( sentry_max_int )

    # Initialize the index of left and right
    index_of_left = 0
    index_of_right = 0



    for i in range(left, right+1, 1):

        if array_left[ index_of_left ] <= array_right[ index_of_right ]:
            # head of array_left is smaller, pop array_left to b

            b[i] = array_left[ index_of_left ]
            index_of_left += 1

        else:


            if sentry_max_int != array_left[ index_of_left ]:
                # those elements in array_left[ index_of_left : mid+1 ] are larger than array_right[ index_of_right ]
                # update and add counter of inversion with ( mid - index_of_left + 1 )

                # print("\n")
                # for j in range(index_of_left, len(array_left)-1 ):
                    
                    # print(" {} > {}".format( array_left[j], array_right[ index_of_right ]) )


                # print("delta", ( len(array_left)-1 - index_of_left ) )
                count_of_inversion += ( len(array_left)-1 - index_of_left )



            # head of array_right is smaller, pop array_right to b
            b[i] = array_right[ index_of_right ]
            index_of_right += 1



    return count_of_inversion


def get_number_of_inversions(a, b, left, right):
    


    # Base case:
    # 1 element, no inversion
    if left == right:
        return 0

    else:

        
        # Divide and Conquer
        mid = (left + right) // 2

        inv_of_left = get_number_of_inversions(a, b, left, mid)
        inv_of_right = get_number_of_inversions(a, b, mid+1, right)
        


        

        # Merge results from sub-problem
        inv_of_merge = merge( a, b, left, mid, right )

        # print("left", inv_of_left)
        # print("right", inv_of_right)
        # print("inv of merge = {}, left = {}, mid = {}, right = {}".format( inv_of_merge, left, mid, right ) )

        sum_of_inv = inv_of_left + inv_of_right + inv_of_merge
        # print("sum of inv", sum_of_inv)

        return sum_of_inv



# Entry point of program
if __name__ == '__main__':

    dbg_swich = False

    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    
    # b is a hard copy of a
    b = list(a)
    print( get_number_of_inversions(a, b, 0, len(a)-1 ) )

    if __debug__ and dbg_swich == True:
        print("a", a)
        print("b", b)








'''

# Development note

# if element of left > element of right, then update counter of inversion
for elem_of_right in array_right:
    count_of_inversion += sum( 1 for elem_of_left in array_left if elem_of_left > elem_of_right )


'''