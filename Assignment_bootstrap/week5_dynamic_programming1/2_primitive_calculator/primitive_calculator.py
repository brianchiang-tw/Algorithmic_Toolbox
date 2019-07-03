# Uses python3
import sys

noNones = lambda fn : lambda *args : fn(a for a in args if a is not None)

def optimal_sequence_dp( n ):

    operations = [ [None] ]*(n+1)
    steps = [0]*(n+1)
    
    current_value = 1
    
    for num in range(1, n+1, 1):
        
        if 1 == num:
            new_operation = list([1])
            operations[1] = new_operation.copy()
            steps[1] = 0

        elif 2 == num:
            new_operation = list([1, 2])
            operations[2] = new_operation.copy()
            steps[2] = 1

        elif 3 == num:
            new_operation = list([1, 3])    
            operations[3] = new_operation.copy()
            steps[3] = 1

        else:

            # Check num is reachable by * 2 or not
            if 0 == num % 2 :
                step_of_mul_2 = steps[ num // 2 ]
            else:
                step_of_mul_2 = None

            # Check num is reachable by * 3 or not
            if 0 == num % 3 :
                step_of_mul_3 = steps[ num // 3 ]    
            else:
                step_of_mul_3 = None

            # num must be reachable by + 1
            step_of_add_1 = steps[ num -1 ]    

            min_of_previous_steps = noNones(min)( step_of_mul_2, step_of_mul_3, step_of_add_1)

            if min_of_previous_steps == step_of_mul_2:
                
                # * 2 is the shorest path to reach num
                steps[num] = steps[ num // 2] + 1

                # update operations of num
                new_operation = operations[ num // 2].copy()
                new_operation.append( num )
                operations[num] = new_operation.copy()

            elif min_of_previous_steps == step_of_mul_3:

                # * 3 is the shorest path to reach num
                steps[num] = steps[ num // 3] + 1

                # update operations of num
                new_operation = operations[ num // 3].copy()
                new_operation.append( num )
                operations[num] = new_operation.copy()

            elif min_of_previous_steps == step_of_add_1:

                 # * 3 is the shorest path to reach num
                steps[num] = steps[ num-1 ] + 1

                # update operations of num
                new_operation = operations[ num-1 ].copy()
                new_operation.append( num )
                operations[num] = new_operation.copy()           

            else:
                print("Error case at {}".format(num) )

                quit()    

    return steps, operations


def optimal_sequence(n):

    steps, series = optimal_sequence_dp(n)

    # Debug message
    # print("steps", steps)
    # print("series", series)

    return series[n]

'''
def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)
'''

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
