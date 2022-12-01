import importlib
import sys
from datetime import datetime

if __name__ == "__main__":
    args = list(map(int, sys.argv[1:]))
    args.sort()

    # default: solve today puzzle
    today = datetime.now()
    solving_year = today.year
    solving_days = [today.day]

    # parse args to get year and days to resolve
    if args:
        # year existing in AoC
        existing_year = 2014 < max(args) <= today.year
        if existing_year:
            solving_year = args.pop()
            solving_days = args
        elif max(args) > 25:
            print(" Wrong arguments.")
            exit()

        # days existing in AoC
        before_christmas = 0 < max(args) < 26 and 0 < min(args) < 26
        before_today = 0 < max(args) <= today.day and 0 < min(args) <= today.day
        if (before_today and solving_year == today.year) or (before_christmas and solving_year != today.year):
            solving_days = args
        else:
            print(" Wrong arguments.")
            exit()

    # use only unique values
    solving_days = list(set(solving_days))

    # import module and print
    for solving_day in solving_days:
        solving_date = str(solving_day).zfill(2) + ".12." + str(solving_year)
        print(solving_date, end=' - ')

        if solving_year == 2022:
            solving_day = str(solving_day).zfill(2)  # new naming

        try:
            a = importlib.import_module("y" + str(solving_year) + ".day" + str(solving_day))
            print("Results :\t\t{:13d},\t{:13d}".format(a.part1(), a.part2()))
        except ModuleNotFoundError:
            print("\t\t\t This solution does not exist")
