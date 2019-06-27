# Uses python3
import sys
import random

# 3 way partition: 
# < pivot, 
# == pivot,
#  > pivot
def partition3(a, left, right):
    #write your code here

    pivot = a[left]

    index_of_less_than = left
    index_of_greater_than = right


    i = left+1
    while i <= right and index_of_less_than != index_of_greater_than:

        if a[i] < pivot:
            a[i], a[index_of_less_than] = a[index_of_less_than], a[i]
            index_of_less_than += 1

        elif a[i] > pivot:
            a[i], a[index_of_greater_than] = a[index_of_greater_than], a[i]
            index_of_greater_than -= 1

            # Give the while loop a chance on next iteration, to check the newly swap element, a[i], is smaller than pivot or not.
            i -= 1

        i += 1


    return index_of_less_than, index_of_greater_than



def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3

    less_than_index, greater_than_index = partition3(a, l, r)

    randomized_quick_sort(a, l, less_than_index-1 )
    randomized_quick_sort(a, greater_than_index+1, r)
    # m = partition2(a, l, r)
    # randomized_quick_sort(a, l, m - 1);
    # randomized_quick_sort(a, m + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
