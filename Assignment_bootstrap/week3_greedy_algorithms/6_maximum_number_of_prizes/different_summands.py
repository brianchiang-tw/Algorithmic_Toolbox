# Uses python3
import sys

def total_sum_of_ascending_series(k):

    # series_sum = 1 + 2 + ... + k = k * ( k + 1) /2
    # this must be a integer, so we adopt integer division here.
    series_sum = k*(k+1)//2

    return series_sum



def optimal_summands(n):
    summands = []
    #write your code here

    upper_bound = int( (2*n)**(1/2)+1 )

    for k in range(1, upper_bound):
        current_sum = total_sum_of_ascending_series( k )
        next_sum = total_sum_of_ascending_series( k+1 )

        if current_sum <= n < next_sum:
            delta =  n - current_sum 

            # make a ascending series from 1 to k (including k)
            summands = list( range(1, k+1) )

            # compensate final term for delta to meets the value of n
            summands[-1] +=  delta
            break


    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
