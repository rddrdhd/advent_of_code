#Task: https://adventofcode.com/2023/day/2
import re
f = open('y2023/data/day02.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]


def get_max_numbers(sets):
    red_cubes = re.findall('[0-9]+ red', sets)
    if len(red_cubes): 
        nums = [int(n.split(" ")[0]) for n in red_cubes]
        max_red = max(nums)
    green_cubes = re.findall('[0-9]+ green', sets)
    if len(green_cubes): 
        nums = [int(n.split(" ")[0]) for n in green_cubes]
        max_green = max(nums)
    blue_cubes = re.findall('[0-9]+ blue', sets)
    if len(blue_cubes): 
        nums = [int(n.split(" ")[0]) for n in blue_cubes]
        max_blue = max(nums)
    return max_red, max_green, max_blue


def part1():
    sum = 0
    for line in lines:
        max_red = 0
        max_green = 0
        max_blue = 0
        _,sets = line.split(":")

        max_red, max_green, max_blue = get_max_numbers(sets)

        if max_red <= 12 and max_green <= 13 and max_blue <= 14:
            sum += int(re.search('[0-9]+', line).group())

    return sum # 2369


def part2():
    sum = 0
    for line in lines:
        min_red = 1
        min_green = 1
        min_blue = 1
        _,sets = line.split(":")

        min_red, min_green, min_blue = get_max_numbers(sets)

        sum += min_red*min_blue*min_green

    return sum # 66363