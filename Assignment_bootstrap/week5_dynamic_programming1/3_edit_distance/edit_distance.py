# Uses python3
import sys



# Output image into console
def print_2d_array( image_matrix, mode = "Hex" ):

    image_height = len( image_matrix )


    image_width = len( image_matrix[0] )


    for y in range( image_height ):
        for x in range( image_width ):

            if "Hex" == mode:
                print( "{:02X}".format( image_matrix[y][x] ), end = ' ' )
            elif "Decimal" == mode:
                print( "{: 10d}".format( image_matrix[y][x] ), end = ' ' )
            else:
                print("Invliad print mode  {:<10} is not supported.".format(mode) )

        print()    

    # One more extra new line in order to keep output neat and tidy
    print("\n")



# function to calculate minimal edit distance with dynamic programming
def edit_distance(s, t):

    #write your code here

    # padding a empty space, denoting empty string, on the head on both s and t
    s = " " + s
    t = " " + t

    height = len(t)
    width = len(s)

    min_edit_dist_array = [ [ 0 for x in range(width) ] for y in range(height) ]

    # The edit with shortest distance from string s to empty string is completed by deleting of all characters of s
    for i in range(width):
        min_edit_dist_array[0][i] = i

    # The edit with shortest distance from string t to empty string is completed by deleting of all characters of t
    for j in range(height):
        min_edit_dist_array[j][0] = j


    # print("after init")
    # print_2d_array(min_edit_dist_array, "Decimal")


    # Main idea of minimal distance with dynamic programming

    # s: the input string
    # t: the input string

    # s-1: substring of s without tail character, where s-1 = s[0:-1]
    # t-1: substring of t without tail character, where t-1 = t[0:-1]

    # If tail character of s and t is equal, 
    #
    # the min edit_dist(s,t) = min  {   
    #                                   edit_dist(s-1, t  ) + cost of deleting tail of s, 
    #                                   edit_dist(s,   t-1) + cost of adding tail of t to s,
    #                                   edit_dist(s-1, t-1) + 0 [ Note: no extra cost due to the equality tail of s = tail of t]
    #                               }
    
    # If tail characters of s and t are different, 
    #
    # the min edit_dist(s,t) = min  {   
    #                                   edit_dist(s-1, t  ) + cost of deleting tail of s, 
    #                                   edit_dist(s,   t-1) + cost of adding tail of t to s,
    #                                   edit_dist(s-1, t-1) + cost of substituting tail of t for tail of s
    #                               }

    for i in range(1, height):
        for j in range(1, width):

            min_edit_dist_by_deletion       = min_edit_dist_array[ i-1 ][ j   ] + 1
            min_edit_dist_by_insertion      = min_edit_dist_array[ i   ][ j-1 ] + 1
            min_edit_dist_by_match          = min_edit_dist_array[ i-1 ][ j-1 ] + 0
            min_edit_dist_by_substitution   = min_edit_dist_array[ i-1 ][ j-1 ] + 1

            if t[i] == s[j]:
                min_edit_dist_array[i][j] = min( min_edit_dist_by_deletion, min_edit_dist_by_insertion, min_edit_dist_by_match )
            else:
                min_edit_dist_array[i][j] = min( min_edit_dist_by_deletion, min_edit_dist_by_insertion, min_edit_dist_by_substitution )



    # print_2d_array(min_edit_dist_array, "Decimal")


    return min_edit_dist_array[ height-1 ][ width-1 ]



# Entry point of program
if __name__ == "__main__":

    input = sys.stdin.read()
    data = list( map(str, input.split() ) )
    # print(data)
    s = data[0]
    t = data[1]
    # s = input()
    # t = input()
    print( edit_distance(s, t) )
