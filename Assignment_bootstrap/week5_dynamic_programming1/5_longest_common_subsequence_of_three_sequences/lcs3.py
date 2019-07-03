#Uses python3
import sys



# function to calculate maximal length of common sequence with dynamic programming
def longest_common_sequence(s, t, u):

    

    # padding a empty zero, denoting empty sequence, on the head on all s, t, and u
    s = [0] + s
    t = [0] + t
    u = [0] + u

    # get length from input s, t, and u
    depth = len(u)
    height = len(t)
    width = len(s)



    # create a 3d array of depth * height * width
    length_of_common_sequence = [ [ [ 0 for x in range(width) ] for y in range(height) ] for z in range(depth) ]


    
    # Main idea of minimal distance with dynamic programming

    # s: the input sequence
    # t: the input sequence
    # u: the input sequence

    # s-1: sub-sequence of s without tail element, where s-1 = s[0:-1]
    # t-1: sub-sequence of t without tail element, where t-1 = t[0:-1]
    # u-1: sub-sequence of t without tail element, where u-1 = u[0:-1]

    # If tail element among s, t and u is equal, 
    #
    # the maximal length_of_common_sequence(s,t) = length_of_common_sequence(s-1, j-1, u-1) + 1 [ Note: +1 is due to the equality tail of s = tail of t = tail of u]
    
    # If tail elements of s, t, and u, are different, 
    #
    # the maximal length_of_common_sequence(s,t) = max  {   
    #                                                       length_of_common_sequence(s-1, t  , u   ) 
    #                                                       length_of_common_sequence(s,   t-1, u   )
    #                                                       length_of_common_sequence(s,   t  , u-1 )
    #                                                   }

    for i in range(0, depth):
        for j in range(0, height):
            for k in range(0, width):


                max_length_of_common_seq_by_deleting_u_tail = length_of_common_sequence[ i-1 ][ j   ][ k   ]
                max_length_of_common_seq_by_deleting_t_tail = length_of_common_sequence[ i   ][ j-1 ][ k   ]
                max_length_of_common_seq_by_deleting_s_tail = length_of_common_sequence[ i   ][ j   ][ k-1 ]
                max_length_of_common_seq_by_match           = length_of_common_sequence[ i-1 ][ j-1 ][ k-1 ] + 1



                if i == 0 or j == 0 or k == 0:
                    # The max length of common sequence between string s to empty string is 0
                    # The max length of common sequence between string t to empty string is 0
                    # The max length of common sequence between string u to empty string is 0
                    length_of_common_sequence[i][j][k] = 0

                elif u[i] == t[j] and t[j] == s[k]:
                    # tail element among s, t and u is equal
                    length_of_common_sequence[i][j][k] = max_length_of_common_seq_by_match

                else:
                    # tail elements of s, t, and u, are different 
                    length_of_common_sequence[i][j][k] = max( max_length_of_common_seq_by_deleting_s_tail, max_length_of_common_seq_by_deleting_t_tail, max_length_of_common_seq_by_deleting_u_tail )


    # output length of longest common sequence of three series
    return length_of_common_sequence[ depth-1 ][ height-1 ][ width-1 ]



# function trigger of longest_common_sequence( a, b, c )
def lcs3(a, b, c):
    
    max_length_of_common_sequence = longest_common_sequence( a, b, c )
    return max_length_of_common_sequence



# Entry point of program
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))

    quit()
