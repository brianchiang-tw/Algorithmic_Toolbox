# Uses python3
import sys

noNones = lambda fn : lambda *args : fn(a for a in args if a is not None)

def get_min_change( price, solution_table ):

    for p in range(0, price+1):
        # print("\n\nprice", p)

        if 0 == p:
            solution_table[p] = ( 0, [] )

        elif 1 == p:
            solution_table[p] = ( 1, [1] )    

        elif 3 == p:
            solution_table[p] = ( 1, [3] )

        elif 4 == p:
            solution_table[p] = ( 1, [4] )

        elif 2 == p:
            solution_table[p] = ( 2, [1, 1])
        
        else:
            
            min_coin_of_price_p_minus_k = noNones(min)(  solution_table[p-1][0],  solution_table[p-3][0], solution_table[p-4][0] )


            if min_coin_of_price_p_minus_k == solution_table[p-1][0]:
                # add a coin with 1 dollar

                container = list( solution_table[p-1][1] )
                container.append(1)
                solution_table[p] = ( min_coin_of_price_p_minus_k + 1, container )

            elif min_coin_of_price_p_minus_k == solution_table[p-3][0]:
                # add a coin of 3 dollar

                container = list( solution_table[p-3][1] )
                container.append(3)
                solution_table[p] = ( min_coin_of_price_p_minus_k + 1, container )

            else:
                # add a coin of 4 dollar

                container = list( solution_table[p-4][1] )
                container.append(4)
                solution_table[p] = ( min_coin_of_price_p_minus_k + 1, container )



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
