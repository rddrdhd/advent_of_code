import importlib
import sys
import time
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
        elif max(args) > 25 or min(args) < 1 :
            print(" Wrong arguments. Use only numbers 1-25 and a year 2014-2025")
            exit()

        # days existing in AoC
        last_day = 25 if solving_year < 2025 else 12
        before_christmas = 0 < max(args) < last_day+1 and 0 < min(args) < last_day+1
        before_today = 0 < max(args) <= today.day and 0 < min(args) <= today.day
        if (before_today and solving_year == today.year) or (before_christmas and solving_year != today.year):
            solving_days = args
        else:
            print(" Wrong arguments. Use only days for which AoC exists.")
            exit()

    # use only unique values
    solving_days = list(set(solving_days))

    print(f"{'Date':<12}      {'Part 1':>16} {'Part 2':>16}     |{'Time P1':>8} {'Time P2':>8}")
    print("-" * 80)

    for solving_day in solving_days:
        solving_year_str = str(solving_year)
        day_str = str(solving_day).zfill(2)
        solving_date = f"{day_str}.12.{solving_year_str}"
        
        print(f"{solving_date} - ", end='')

        try:
            module_name = f"y{solving_year_str}.day{day_str}"
            a = importlib.import_module(module_name)

            t0 = time.perf_counter()
            p1 = a.part1()
            t1 = time.perf_counter()
            time_p1 = t1 - t0

            t0 = time.perf_counter()
            p2 = a.part2()
            t1 = time.perf_counter()
            time_p2 = t1 - t0

            out_p1 = str(p1)
            out_p2 = str(p2)
            
            print(f"Results: {out_p1:>16} {out_p2:>16} | {time_p1:6.4f}s {time_p2:6.4f}s")

        except ModuleNotFoundError:
            print(f"Results: {'(No Solution)':>16} {'-':>16} | {'-':>7}  {'-':>7}")
        except Exception as e:
            # Catch other errors (like code failing) to keep the loop running
            print(f"Error: {str(e)}")
        