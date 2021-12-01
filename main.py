import sys
from typing import Match
from datetime import datetime


if __name__ == "__main__":
    args = list(map(int, sys.argv[1:]))
    args.sort()
    
    today = datetime.now().day

    if len(args) == 0:
        args.append( today )

    if max(args) > today :
        print("Realy? {}? This task is not out yet...".format( max(args) ))

    if 1 in args :
        import day1 as d1
        print("01.12- - Results:\t\t{},\t{}".format( d1.part1(), d1.part2() ))

    if 2 in args :
        import day2 as d2
        #print("02.12- - Result:\t\t\t", d2.part1() )
