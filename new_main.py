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
        if 2014 < max(args) < today.year:
            solving_year = args.pop()
            solving_days = args
        if 0 < max(args) < 26 and 0 < min(args) < 26:
            solving_days = args
        else:
            print(" Wrong arguments. Enter days to solve or nothing for today. \n Days should be between 1 and 25.")
            exit()

    # use only unique values
    solving_days = list(set(solving_days))

    # import module and print
    for solving_day in solving_days:
        solving_date = str(solving_day).zfill(2)+".12."+str(solving_year)
        print(solving_date, end=' - ')
        try:
            a = importlib.import_module("y"+str(solving_year)+".day"+str(solving_day))
            print("Results:\t\t{},\t{}".format(a.part1(), a.part2()))
        except ModuleNotFoundError:
            print("This solution does not exist")