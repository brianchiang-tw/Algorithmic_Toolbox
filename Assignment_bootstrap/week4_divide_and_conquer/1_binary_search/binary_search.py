# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    


    # short-cut of value out of upper bound and lower bound
    max_of_array = a[-1]
    min_of_array = a[0]

    # print("min", min_of_array)
    # print("max", max_of_array)

    if x < min_of_array or x > max_of_array:
        return -1
    
    # short-cut of hit on min value
    if x == min_of_array:
        return 0
    
    # short-cut of hit on max value
    if x == max_of_array:
        return ( len(a)-1 )
    

    while( left <= right ):

        # update mid on each iteration
        mid = left + (right-left) // 2

        if x < a[mid]:
            right = mid-1

        elif x > a[mid]:
            left = mid + 1

        else:
            # hit on x == a[mid]
            return mid



    # cannot find x in a
    return -1



def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
