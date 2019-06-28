# Uses python3
import sys
import random



# support function: less_than
def less_than( num_1, num_2, label_1, label_2 ):
    if ( num_1 < num_2 ) or ( num_1 == num_2 and label_1 < label_2 ):
        return True
    else:
        return False



#  support funciton: equal
def equal_to( num_1, num_2, label_1, label_2 ):
    if ( num_1 == num_2 ) and ( label_1 == label_2 ):
        return True
    else:
        return False



# support function
def less_than_or_equal_to( num_1, num_2, label_1, label_2):
    
    if less_than( num_1, num_2, label_1, label_2 ) or equal_to( num_1, num_2, label_1, label_2 ):
        return True
    else:
        return False



# support funciton: 3 way partition of customized quicksort over pair (number, label)
def partition_3way( array_num, array_label, left, right):

    # initialize pivot of number and label
    pivot_of_number = array_num[left]
    pivot_of_label = array_label[left]

    # initialize boundary of less-than and greater-than
    boundary_of_less_than = left+1
    boundary_of_greater_than = left

    for i in range(left+1, right+1):

        if less_than_or_equal_to( array_num[i], pivot_of_number, array_label[i], pivot_of_label ):

            boundary_of_greater_than += 1

            # swap
            array_num[i], array_num[boundary_of_greater_than] = array_num[boundary_of_greater_than], array_num[i]
            array_label[i], array_label[boundary_of_greater_than] = array_label[boundary_of_greater_than], array_label[i]


            if less_than( array_num[boundary_of_greater_than], pivot_of_number, array_label[boundary_of_greater_than], pivot_of_label ):

                # swap
                array_num[boundary_of_less_than], array_num[boundary_of_greater_than] = array_num[boundary_of_greater_than], array_num[boundary_of_less_than]
                array_label[boundary_of_less_than], array_label[boundary_of_greater_than] = array_label[boundary_of_greater_than], array_label[boundary_of_less_than]

                boundary_of_less_than += 1


    array_num[left], array_num[ boundary_of_less_than-1 ], array_num[ boundary_of_less_than-1 ], array_num[left]
    array_label[left], array_num[ boundary_of_less_than-1 ], array_label[ boundary_of_less_than-1 ], array_label[left]


    return boundary_of_less_than, boundary_of_greater_than



# support function: customized quicksort over pair (number, label)
def randomized_quick_sort( array_num, array_label, left, right):

    if left >= right:
        return

    random_index = random.randint(left, right)

    # swap
    array_num[left], array_num[random_index] = array_num[random_index], array_num[left]
    array_label[left], array_label[random_index] = array_label[random_index], array_label[left]

    # Divide and conquer with 3-way partition
    boundary_of_less_than, boundary_of_greater_than = partition_3way( array_num, array_label, left, right)

    randomized_quick_sort( array_num, array_label, left, boundary_of_less_than-1 )
    randomized_quick_sort( array_num, array_label, boundary_of_greater_than+1, right )

    return



def fast_count_segments(starts, ends, points):

    # a container for counting covering of segments
    cnt = [0] * len(points)
    
    # Definition of label for left end of segment, point coordination, and right end of segment.
    S_LEFT = -1
    PT_POINT = 0
    S_RIGHT = 1

    
    starts_label = [ S_LEFT ] * len( starts )
    ends_label = [ S_RIGHT ] * len( ends )
    points_label = [ PT_POINT ] * len( points )

    array_of_coordination = starts + ends + points
    array_of_label = starts_label + ends_label + points_label

    # launch quicksort to sort coordination and label on ascending order
    randomized_quick_sort( array_of_coordination, array_of_label, 0, len(array_of_coordination)-1 )

    # a dynamic self-updating counter for covering segment
    total_count_of_current_covering_segment = 0

    # a dictionary for point <-> total count of covering segment relationship
    point_coverage = {}

    # initialize point coverage to zero
    for p in points:
        point_coverage[p] = 0

    # print("dict", point_coverage )

    for index in range( len(array_of_coordination) ):

        if array_of_label[ index ] == S_LEFT:
            # Entering a interval of a segment, update and add 1 to counter
            total_count_of_current_covering_segment += 1

        elif array_of_label[ index ] == S_RIGHT:
            # Leaving a interval of a segment, update and minus 1 from counter
            total_count_of_current_covering_segment -= 1
        
        elif array_of_label[ index ] == PT_POINT:

            if point_coverage[ array_of_coordination[index] ] == 0: 
                point_coverage[ array_of_coordination[index] ] += total_count_of_current_covering_segment



    # print("dict", point_coverage )


    # print("points", points )
    # Write final statistic of covering segment of each point back to container cnt
    for i in range( len(points) ):
        # key_of_pt =  points[i]
        # print("key pt", key_of_pt )
        # print("val cover", point_coverage[ key_of_pt ] )
        cnt[i] = point_coverage[ points[i] ]


    return cnt



def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt



# Entry point of program
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    #use fast_count_segments
    # cnt = naive_count_segments(starts, ends, points)

    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
