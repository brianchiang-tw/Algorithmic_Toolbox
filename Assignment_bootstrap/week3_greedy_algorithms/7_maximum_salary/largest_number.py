#Uses python3

import sys

# Pick the larger leading one between digits and max_digit
def isGreaterOrEqual(digits, max_digit):

    value_of_digits_on_leading = int( digits + max_digit )
    value_of_max_digits_on_leading = int( max_digit + digits )

    if value_of_digits_on_leading >= value_of_max_digits_on_leading:
        return True
    else:
        return False



def largest_number(a):
    #write your code here

    largest_num = ""

    # while a is not empty
    while len(a) >=1 :
        max_digit = "0"
   
        # visit and check each digits
        for digits in a:
            
            # update max_digit
            if isGreaterOrEqual(digits, max_digit):
                max_digit = digits

        # append max digit into largest_num
        largest_num = largest_num + max_digit
    
        # remove max digit from a
        a.remove(max_digit)



    return largest_num

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
