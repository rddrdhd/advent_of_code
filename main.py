import sys
from datetime import datetime

if __name__ == "__main__":
    print("")
    args = list(map(int, sys.argv[1:]))
    args.sort()

    if len(args):
        if args[0] > 2019:
            year = args.pop()

    today = datetime.now().day

    if len(args) == 0:
        args.append(today)

    if max(args) == 2020:

        if 1 in args:
            from y2020 import day1

            print("01.12.2020 - Results:\t\t{},\t{}".format(day1.part1(), day1.part2()))

        if 2 in args:
            from y2020 import day2

            print("02.12.2020 - Results:\t\t{},\t{}".format(day2.part1(), day2.part2()))

        if 3 in args:
            from y2020 import day3

            print("03.12.2020 - Results:\t\t{},\t{}".format(day3.part1(), day3.part2()))

        if 4 in args:
            from y2020 import day4

            print("04.12.2020 - Results:\t\t{},\t{}".format(day4.part1(), day4.part2()))

        if 5 in args:
            from y2020 import day5

            print("05.12.2020 - Results:\t\t{},\t{}".format(day5.part1(), day5.part2()))

        if 10 in args:
            from y2020 import day10

            print("10.12.2020 - Results:\t\t{},\t{}".format(day10.part1(), day10.part2()))

        elif max(args) > today:
            print("NOPE...".format(max(args)))

    else:

        if 1 in args:
            from y2021 import day1 as d

            print("01.12.2021 - Results:\t\t{},\t{}".format(d.part1(), d.part2()))

        if 2 in args:
            from y2021 import day2 as d

            print("02.12.2021 - Results:\t\t{},\t{}".format(d.part1(), d.part2()))

        if 3 in args:
            from y2021 import day3 as d

            print("03.12.2021 - Results:\t\t{},\t{}".format(d.part1(), d.part2()))

        if 4 in args:
            from y2021 import day4p1 as d1
            from y2021 import day4p2 as d2

            print("04.12.2021 - Results:\t\t{},\t{}".format(d1.part1(), d2.part2()))

        if 5 in args:
            from y2021 import day5 as d

            print("05.12.2021 - Results:\t\t{},\t{}".format(d.part1(), d.part2()))

        if 6 in args:
            from y2021 import day6 as d

            print("06.12.2021 - Results:\t\t{},\t{}".format(d.part1(), d.part2()))

        if 7 in args:
            from y2021 import day7 as d

            print("07.12.2021 - Results:\t\t{},\t{}".format(d.part1(), d.part2()))

        if 8 in args:
            from y2021 import day8 as d

            print("08.12.2021 - Results:\t\t{},\t{}".format(d.part1(), d.part2()))
        if 9 in args:
            from y2021 import day9 as d

            print("09.12.2021 - Results:\t\t{},\t{}".format(d.part1(), d.part2()))

        elif max(args) > today:
            print("NOPE...".format(max(args)))
