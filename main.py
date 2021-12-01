import sys
from typing import Match

if __name__ == "__main__":
    args = list(map(int, sys.argv[1:]))

    if( 1 in args ):
        import day1 as d1
        print("01 - Results:\t\t{},\t{}".format(d1.part1(),d1.part2()))
    if( 2 in args ):
        import day2 as d2
        print("02 - Result:\t\t0",d2.part1())
