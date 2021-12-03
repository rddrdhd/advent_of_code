# https://adventofcode.com/2021/day/3

f = open('y2021/data/day3.txt', 'r')
lines = f.readlines()
f.close()


def part1():
    counter = [0 for _ in range(len(lines[0].strip()))]
    gamma_rate = "0b"
    consumption_rate = "0b"

    for line in lines:
        for position in range(len(line.strip())):
            counter[position] += int(line[position])

    for position_count in counter:
        if position_count > int(len(lines) / 2):  # 1 is most used on this position
            gamma_rate += "1"
            consumption_rate += "0"
        else:
            gamma_rate += "0"
            consumption_rate += "1"

    return int(gamma_rate, 2) * int(consumption_rate, 2)


def part2():
    count = 0
    return count
