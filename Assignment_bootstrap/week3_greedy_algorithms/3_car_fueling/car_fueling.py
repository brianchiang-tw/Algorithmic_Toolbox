# python3
import sys

def get_reachable_gas_station( current_position, miles_to_empty, stops ):

    reachable_gas_station = []

    for gas_station_position in stops:

        # keep going further, instead of being on reverse direction
        if (gas_station_position > current_position) and (gas_station_position - current_position) <= miles_to_empty:
            reachable_gas_station.append( gas_station_position )
            # stops.remove( gas_station_position )


    # print("\n\n")
    # print("currnet_position", current_position)
    # print("miles_to_empty", miles_to_empty)
    # print("stops", stops )
    # print("reachable_gas_station", reachable_gas_station)


    if not reachable_gas_station:
        # cannot reach next gas station from current positiotn
        return [-1]
    else:
        return reachable_gas_station



# core function to compute min refuel times
def compute_min_refills(distance, tank, stops):
    
    # number_of_gas_stations = len( stops )

    # initialize current_position as start point 0 miles
    last_refuel_position = 0

    # initialize furthest_travel_range to (0 + tank) miles
    furthest_travel_range = 0 + tank

    # initialize times of refuel to 0
    times_of_refuel = 0

    # keeps going until meets the end
    while furthest_travel_range < distance:

        gas_station_in_range = get_reachable_gas_station(last_refuel_position, tank, stops)

        # minimize the times of refuel by going as futher as possible
        furthest_refuel_stop = max( gas_station_in_range )
        # print("furthest refuel stop", furthest_refuel_stop)



        if -1 == furthest_refuel_stop:
            # this car cannot reach the end
            return -1
        else:
            

            # refules in gas station with furthest_refuel_stop (on miles)
            last_refuel_position = furthest_refuel_stop

            # update furtjest travel range
            furthest_travel_range = last_refuel_position + tank

            # update times of refuel
            times_of_refuel += 1
    
            # remove pass_through_station from stops (i.e., all gas station)
            for pass_through_station in gas_station_in_range:
                stops.remove( pass_through_station )




    return times_of_refuel



# Entry point of program
if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
