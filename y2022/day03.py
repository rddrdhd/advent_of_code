# Task: https://adventofcode.com/2022/day/3
f = open('y2022/data/day03.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]
priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def part1():
    sum = 0
    for line in lines:
        half_index = int(len(line) / 2)
        f_half, s_half = line[:half_index], line[half_index:]
        found_char = ""
        for i, char in enumerate(f_half):
            if len(found_char): break
            if f_half[i] in s_half:
                found_char = char
                sum += priorities.rfind(char) + 1

    return sum


def part2():
    sum = 0
    print(len(lines))
    for i in range(0, len(lines) - 1, 3):
        f_third = lines[i]
        s_third = lines[i + 1]
        t_third = lines[i + 2]
        found_char = ""
        for j, char in enumerate(f_third):
            if len(found_char): break
            if f_third[j] in s_third:
                for k in range(len(s_third)):
                    if len(found_char): break
                    if s_third[k] in t_third:
                        found_char = char
                        print(char)
                        sum += priorities.rfind(char) + 1
    # 2853 to neni
    return sum
