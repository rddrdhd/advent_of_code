# Task: https://adventofcode.com/2022/day/4
import re

f = open('y2022/data/day04.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]


def part1():
    sum = 0
    for line in lines:
        a, b, c, d = [int(s) for s in re.findall(r'\b\d+\b', line)]
        range_1 = [*range(int(a), int(b) + 1)]
        range_2 = [*range(int(c), int(d) + 1)]
        a12 = range_1 + range_2
        duplicates = [number for number in a12 if a12.count(number) > 1]
        if (duplicates):
            unique_duplicates = list(set(duplicates))
            if len(unique_duplicates) == len(range_1) or len(unique_duplicates) == len(range_2):
                sum += 1
    return sum  # 536


def part2():
    sum = 0
    for line in lines:
        a, b, c, d = [int(s) for s in re.findall(r'\b\d+\b', line)]
        range_1 = [*range(int(a), int(b) + 1)]
        range_2 = [*range(int(c), int(d) + 1)]
        a12 = range_1 + range_2
        duplicates = [number for number in a12 if a12.count(number) > 1]
        if duplicates:
            sum += 1
    return sum  # 845
