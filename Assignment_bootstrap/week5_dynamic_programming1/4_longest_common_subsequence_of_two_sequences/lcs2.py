#Uses python3
import sys



# function to calculate maximal length of common sequence with dynamic programming
def longest_common_sequence(s, t):

    

    # padding a empty zero, denoting empty sequence, on the head on both s and t
    s = [0] + s
    t = [0] + t

    height = len(t)
    width = len(s)

    length_of_common_sequence = [ [ 0 for x in range(width) ] for y in range(height) ]

    # The max length of common sequence between string s to empty string is 0
    for i in range(width):
        length_of_common_sequence[0][i] = 0

    # The max length of common sequence between string t to empty string is 0
    for j in range(height):
        length_of_common_sequence[j][0] = 0


    # print("after init")
    # print_2d_array(length_of_common_sequence, "Decimal")


    # Main idea of minimal distance with dynamic programming

    # s: the input string
    # t: the input string

    # s-1: substring of s without tail character, where s-1 = s[0:-1]
    # t-1: substring of t without tail character, where t-1 = t[0:-1]

    # If tail character of s and t is equal, 
    #
    # the maximal length_of_common_sequence(s,t) = length_of_common_sequence(s-1, j-1) + 1 [ Note: +1 is due to the equality tail of s = tail of t]
    
    # If tail characters of s and t are different, 
    #
    # the maximal length_of_common_sequence(s,t) = max  {   
    #                                                       length_of_common_sequence(s-1, t  )
    #                                                       length_of_common_sequence(s,   t-1)
    #                                                   }

    for i in range(1, height):
        for j in range(1, width):

            max_length_of_common_seq_by_deleting_t_tail = length_of_common_sequence[ i-1 ][ j   ]
            max_length_of_common_seq_by_deleting_s_tail = length_of_common_sequence[ i   ][ j-1 ]
            max_length_of_common_seq_by_match           = length_of_common_sequence[ i-1 ][ j-1 ] + 1

            if t[i] == s[j]:
                length_of_common_sequence[i][j] = max_length_of_common_seq_by_match
            else:
                length_of_common_sequence[i][j] = max( max_length_of_common_seq_by_deleting_t_tail, max_length_of_common_seq_by_deleting_s_tail )



    # print_2d_array(length_of_common_sequence, "Decimal")


    return length_of_common_sequence[ height-1 ][ width-1 ]



# function trigger of longest_common_sequence( a, b)
def lcs2(a, b):
    #write your code here

    # print("a", a )    
    # print("b", b )

    max_length_of_common_sequence = longest_common_sequence( a, b )
    return max_length_of_common_sequence



# Entry point of program
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
