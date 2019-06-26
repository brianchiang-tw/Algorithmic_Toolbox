# Uses python3
import sys
import operator

from collections import namedtuple

Segment = namedtuple('Segment', 'start end')



def optimal_points(segments):

    # a list of integer points, which are of highest coverd over segment 
    coverage_points = []

    # Sort by end point position of each segment, on ascending order
    segments = sorted( segments, key = lambda s: (s.end), reverse = False )

    
    # update current coverage point as first segment's end point
    current_coverage_point = segments[0].end

    # add current coverage point into coverage_points
    coverage_points.append( current_coverage_point )

    for seg in segments:

        if current_coverage_point < seg.start:

            # update current coverage point when old one cannot cover new segment on the right hand side
            current_coverage_point = seg.end

            # add current coverage point into coverage_points
            coverage_points.append( current_coverage_point )

        else:

            # this segment is covered by current coverage point, no need to update
            pass

    return coverage_points

# Entry of program
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())

    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)

    print(len(points))
    for p in points:
        print(p, end=' ')



