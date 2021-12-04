import sys
from datetime import datetime


if __name__ == "__main__":
    print("")
    args = list(map(int, sys.argv[1:]))
    args.sort()

    if(args[0] > 2019):
        args = args[1:]
    
    today = datetime.now().day

    if len(args) == 0:
        args.append( today )

    if max(args) == 2020:
        
        if 1 in args :
            from y2020 import day1
            print("01.12.2020 - Results:\t\t{},\t{}".format( day1.part1(), day1.part2() ))
        
        if 2 in args :
            from y2020 import day2
            print("02.12.2020 - Results:\t\t{},\t{}".format( day2.part1(), day2.part2() ))

        if 3 in args :
            from y2020 import day3
            print("03.12.2020 - Results:\t\t{},\t{}".format( day3.part1(), day3.part2() ))

        if 4 in args :
            from y2020 import day4
            print("04.12.2020 - Results:\t\t{},\t{}".format( day4.part1(), day4.part2() ))


    elif max(args) > today :
        print("{}? NOPE...".format( max(args) ))

    else:

        if 1 in args :
            from y2021 import day1
            print("01.12.2021 - Results:\t\t{},\t{}".format( day1.part1(), day1.part2() ))

        if 2 in args :
            from y2021 import day2
            print("02.12.2021 - Results:\t\t{},\t{}".format( day2.part1(), day2.part2() ))

        if 3 in args :
            from y2021 import day3
            print("03.12.2021 - Results:\t\t{},\t{}".format( day3.part1(), day3.part2() ))
        if 4 in args :
            from y2021 import day4
            print("04.12.2021 - Results:\t\t{},\t{}".format( day4.part1(), day4.part2() ))
