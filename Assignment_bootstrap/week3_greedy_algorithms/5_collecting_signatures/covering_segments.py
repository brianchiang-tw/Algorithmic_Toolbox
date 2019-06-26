# Uses python3
import sys
import operator

from collections import namedtuple

Segment = namedtuple('Segment', 'start end')



def make_point_set( segments ):

    container_of_ps=[]
    
    for single_segment in segments:
        
        points_of_segment=set()

        for integer in range(single_segment.start, single_segment.end+1 ):
            points_of_segment.add(integer)
    
        container_of_ps.append( points_of_segment )

    return container_of_ps




def optimal_points(segments):

    # a list of integer points, which are of highest coverd over segment 
    points = []
    
    # a container of point sets
    # container_of_ps = make_point_set( segments )

    # a set of covered segment
    container_of_covered_segment = set()


    total_number_of_segment = len(segments)

    while len(container_of_covered_segment) != total_number_of_segment:


        # a dictionary: integer point maps the number of covered segment
        dict_intpt_to_num_of_seg = {}

        # for each integer point in interval segment[0].start ~ segment[0].end
        for integer_point in range(segments[0].start, segments[0].end+1):

            # visit each segment
            for s in segments:

                if s.start <= integer_point <= s.end :

                    # update the dict: dict_intpt_to_num_of_seg
                    dict_intpt_to_num_of_seg[integer_point] = dict_intpt_to_num_of_seg.get(integer_point, 0) + 1
                        

        # Get the integer_point, coming from segments[0], with highest cover over all segment
        integer_point_of_higest_cover = max(dict_intpt_to_num_of_seg.items(), key=operator.itemgetter(1))[0]   

        # add the integer point into points set
        print("add integer point with highest cover:", integer_point_of_higest_cover)
        points.append( integer_point_of_higest_cover )     

        # remove those segements which are covered by the point
        # add them into container_of_covered_segment
        check_index = 0
        while True:

            # If segments is empty, then we finish the task of finding integer point of highest covering over segments
            # If check index meets the length, then we have check all the segments on this iteration
            if not segments or check_index == len(segments):
                break

            seg = segments[check_index]

            if seg.start <= integer_point_of_higest_cover <= seg.end:
                container_of_covered_segment.add(seg)
                segments.remove(seg)
                print("add covered segment:", seg )
            else:
                check_index += 1

            

    return points

# Entry of program
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())

    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)

    print(len(points))
    for p in points:
        print(p, end=' ')
