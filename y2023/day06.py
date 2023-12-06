#Task: https://adventofcode.com/2023/day/6
import re
f = open('y2023/data/day06.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]

def get_ways(time_nums, distance_nums):
    ways = []
    for race_num in range(len(time_nums)):
        race_time = int(time_nums[race_num])
        race_distance_record = int(distance_nums[race_num])

        press_button_time = 1
        count_ways = 0
        while press_button_time < race_time:
            new_race_time = race_time - press_button_time
            speed = press_button_time
            if new_race_time*speed > race_distance_record:
                count_ways += 1
            press_button_time += 1
        ways.append(count_ways)
    return ways


def part1():
    prod = 1
    time_nums = lines[0].split()[1:]
    distance_nums = lines[1].split()[1:]
    ways = get_ways(time_nums, distance_nums)
    for way in ways:
        prod *= way
    return prod # 170000

def part2():
    prod = 1
    # using an array with one item, because why not
    time_nums=[int("".join(lines[0].split(" ")[1:]))]
    distance_nums=[int("".join(lines[1].split(" ")[1:]))]
    ways = get_ways(time_nums, distance_nums)
    for way in ways:
        prod *= way
    return prod # 20537782
