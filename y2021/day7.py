# Task: https://adventofcode.com/2021/day/7
import numpy

f = open('y2021/data/day7.txt', 'r')
lines = f.readlines()
f.close()


def part1():
    numbers = list(map(int, lines[0].split(",")))
    burned_fuel = []
    for i in range(max(numbers)):
        burned_fuel.append(0)
        for num in numbers:
            burned_fuel[i] += abs(num - i)
    return min(burned_fuel)  # 339321


def triangle(n):
    return int(((n ** 2) + n) / 2)


def part2():
    numbers = list(map(int, lines[0].split(",")))
    burned_fuel = []
    for i in range(max(numbers)):
        burned_fuel.append(0)
        for num in numbers:
            difference = abs(num - i)
            sum_d = triangle(difference)
            burned_fuel[i] += sum_d
    return min(burned_fuel)  # 95476244
