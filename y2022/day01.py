#Task: https://adventofcode.com/2022/day/1
f = open('y2022/data/day01.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]

def part1():
    elf_calories = 0
    max_calories = 0
    for i, line in enumerate(lines):
        if line != "":
            elf_calories += int(line)
        else:
            if elf_calories > max_calories:
                max_calories = elf_calories
            elf_calories = 0
    return max_calories


def part2():
    elves_calories = []
    elf_calories = 0
    for line in lines:
        if line != "":
            elf_calories += int(line)
        else:
            elves_calories.append(elf_calories)
            elf_calories = 0
    e = sorted(elves_calories)
    return e[-1]+e[-2]+e[-3]
