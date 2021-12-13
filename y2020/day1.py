# Task: https://adventofcode.com/2020/day/1

f = open('y2020/data/day1.txt', 'r')
lines = f.readlines()
f.close()


def part1():
    for line1 in lines:
        for line2 in lines:
            line_1 = int(line1.strip())
            line_2 = int(line2.strip())
            if line_1 + line_2 == 2020:
                return line_1 * line_2  # 840324


def part2():
    for line1 in lines:
        for line2 in lines:
            for line3 in lines:
                line_1 = int(line1.strip())
                line_2 = int(line2.strip())
                line_3 = int(line3.strip())
                if line_1 + line_2 + line_3 == 2020:
                    return line_1 * line_2 * line_3  # 170098110
