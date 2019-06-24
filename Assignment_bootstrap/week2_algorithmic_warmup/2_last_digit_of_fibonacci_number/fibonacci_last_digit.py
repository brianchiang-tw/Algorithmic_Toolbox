# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current % 10, (previous + current) % 10

    return current



# Entry point of program
if __name__ == '__main__':
   
    n = int( input() )

    # print("n:", n )

    print(get_fibonacci_last_digit_naive(n))
