# Task: https://adventofcode.com/2021/day/6
import copy
f = open('y2021/data/day6.txt', 'r')
lines = f.readlines()
f.close()

# Each day, a 0 becomes a 6 and adds a new 8.
# while each other number decreases by 1 if it was present at the start of the day.

def new_part1(days_to_count = 18):
    lanternfish_dtls = lines[0].strip().split(",")
    dtl_counter = [0 for _ in range(9)]
    for fish_dtgb in lanternfish_dtls:
        dtl_counter[int(fish_dtgb)] += 1

    new_counter = copy.copy(dtl_counter)
    while days_to_count:
        dtl = copy.copy(new_counter)
        for day_to_give_birth in range(len(dtl) - 1, -1, -1):
            new_counter[day_to_give_birth - 1] = dtl[day_to_give_birth]
            if day_to_give_birth == 0:
                new_counter[6] += dtl[day_to_give_birth]
        days_to_count -= 1
    return sum(new_counter)


def part1(days_to_count=80):

    lanternfish = lines[0].strip().split(",")

    for day in range(days_to_count):
        for fish_id in range(len(lanternfish)):
            fish_count = int(lanternfish[fish_id]) - 1
            if fish_count == -1:
                fish_count = 6
                lanternfish.append(8)

            lanternfish[fish_id] = fish_count

    count = len(lanternfish)
    return count



def part2(days_to_count=256):
    return new_part1(256)

