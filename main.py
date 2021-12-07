import sys
from datetime import datetime

if __name__ == "__main__":
    print("")
    args = list(map(int, sys.argv[1:]))
    args.sort()

    if len(args):
        if args[0] > 2019:
            args = args[1:]

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
            from y2021 import day1

            print("01.12.2021 - Results:\t\t{},\t{}".format(day1.part1(), day1.part2()))

        if 2 in args:
            from y2021 import day2

            print("02.12.2021 - Results:\t\t{},\t{}".format(day2.part1(), day2.part2()))

        if 3 in args:
            from y2021 import day3

            print("03.12.2021 - Results:\t\t{},\t{}".format(day3.part1(), day3.part2()))

        if 4 in args:
            from y2021 import day4p1
            from y2021 import day4p2

            print("04.12.2021 - Results:\t\t{},\t{}".format(day4p1.part1(), day4p2.part2()))

        if 5 in args:
            from y2021 import day5

            print("05.12.2021 - Results:\t\t{},\t{}".format(day5.part1(), day5.part2()))

        if 6 in args:
            from y2021 import day6

            print("06.12.2021 - Results:\t\t{},\t{}".format(day6.part1(), day6.part2()))

        if 7 in args:
            from y2021 import day7

            print("07.12.2021 - Results:\t\t{},\t{}".format(day7.part1(), day7.part2()))

        elif max(args) > today:
            print("NOPE...".format(max(args)))
