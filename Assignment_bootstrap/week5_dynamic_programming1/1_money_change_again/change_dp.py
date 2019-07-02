# Uses python3
import sys

noNones = lambda fn : lambda *args : fn(a for a in args if a is not None)

def get_min_change( price, solution_table ):

    for p in range(0, price+1):
        # print("\n\nprice", p)

        if 0 == p:
            solution_table[p] = ( 0, [] )
            # print("sol at p",  solution_table[p] )

        elif 1 == p:
            solution_table[p] = ( 1, [1] )    
            # print("sol at p",  solution_table[p] )

        elif 3 == p:
            solution_table[p] = ( 1, [3] )
            # print("sol at p",  solution_table[p] )

        elif 4 == p:
            solution_table[p] = ( 1, [4] )
            # print("sol at p",  solution_table[p] )

        elif 2 == p:
            solution_table[p] = ( 2, [1, 1])
            # print("sol at p",  solution_table[p] )
        
        else:
            
            min_coin_of_price_p_minus_k = noNones(min)(  solution_table[p-1][0],  solution_table[p-3][0], solution_table[p-4][0] )
            # print("min_coin_of_price_p_minus_k:", min_coin_of_price_p_minus_k)


            if min_coin_of_price_p_minus_k == solution_table[p-1][0]:
                # print("add 1")
                # add a coin with 1 dollar

                # print("container of p-1", solution_table[p-1][1] )
                container = list( solution_table[p-1][1] )
                container.append(1)
                # print("container of p", container)
                solution_table[p] = ( min_coin_of_price_p_minus_k + 1, container )
                # print("sol at p",  solution_table[p] )

            elif min_coin_of_price_p_minus_k == solution_table[p-3][0]:
                # print("add 3")
                # add a coin of 3 dollar

                # print("p", p)
                # print( solution_table[p-3] )
                container = list( solution_table[p-3][1] )
                # print("before adding 3")
                # print("container", container)
                container.append(3)
                solution_table[p] = ( min_coin_of_price_p_minus_k + 1, container )
                # print("sol at p",  solution_table[p] )

            else:


                container = list( solution_table[p-4][1] )
                # print("before adding 4")
                container.append(4)
                # print("add 4")
                # add a coin of 4 dollar
                solution_table[p] = ( min_coin_of_price_p_minus_k + 1, container )
                # print("sol at p",  solution_table[p] )


        # print("sol table", solution_table )

    return solution_table[price][0], solution_table[price][1]

def get_change(m):
    #write your code here

    lookup_table = [(None, None)]*(m+1)

    min_coins, coin_container = get_min_change( price = m, solution_table = lookup_table)

    # print("coins container", coin_container)
    # print("sum of coins", sum(coin_container) )

    return min_coins

if __name__ == '__main__':
    m = int(sys.stdin.read())

    print( get_change(m) )
