# Task: https://adventofcode.com/2021/day/2

f = open('y2021/data/day02.txt', 'r')
lines = f.readlines()
f.close()


def part1():
    depth = 0
    distance = 0
    for line in lines:
        command, value = line.strip().split(" ")
        if command == "down":
            depth += int(value)
        if command == "up":
            depth -= int(value)
        if command == "forward":
            distance += int(value)
    return depth * distance  # 1654760


def part2():
    depth = 0
    distance = 0
    aim = 0
    for line in lines:
        command, value = line.strip().split(" ")
        if command == "down":
            aim += int(value)
        if command == "up":
            aim -= int(value)
        if command == "forward":
            distance += int(value)
            depth += int(aim) * int(value)
    return depth * distance  # 1956047400
