# Uses python3
import sys


def get_maj(a, left, right):

    # Base case:
    # One element:
    if left == right:

        # only one, majority is itself.
        return a[left]



    # Base case:
    # Two elements
    if left+1 == right:

        if a[left] == a[right]:
            # both are the same, and it's majority of these two 
            return a[left]

        else:
            # both are different, no majority
            return None



    # Divide 
    mid = left + ( right - left ) // 2

    major_left_half = get_maj(a, left, mid)
    major_right_half = get_maj(a, mid+1, right)

    # Conquer

    # Majority element is the same on both sides
    if major_left_half == major_right_half:
        return major_left_half

    else:
        # Majority elements are dufferent on both sides
        # Pick the one with occurrence > n/2



        sub_array = a[left:right+1]
        len_of_sub_array = len(sub_array)

        majority_threshold = len_of_sub_array // 2 + 1

        count_of_left_major = sub_array.count( major_left_half )
        count_of_right_major =  sub_array.count( major_right_half )


        # print()
        # print("left", left)
        # print("right", right)
        # print("sub array", sub_array)
        # print("th", majority_threshold)



        if count_of_left_major >= majority_threshold:
            return major_left_half
        
        elif count_of_right_major >= majority_threshold:
            return major_right_half

        else:
            return None
    

def get_majority_element(a, left, right):
    # if left == right:
    #     return -1
    # if left + 1 == right:
    #     return a[left]


    #write your code here
    majority = get_maj(a, left, right)

    if None != majority:
        return majority
    
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element( a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
