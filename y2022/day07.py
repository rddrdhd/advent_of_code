# Task: https://adventofcode.com/2022/day/6
f = open('y2022/data/day07.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]


def part1():
    current_dir = []  # empty means /
    structure = {}

    for line in lines:
        if line[0] == "$":
            print("stop reading ls")

        if line == '$ ls':
            # update structure
            print("start reading")
        else:
            # move through directories
            if line == '$ cd /':
                current_dir = []
            elif "cd" in line:
                directory = line[5:]
                if directory == "..":
                    current_dir.pop()
                else:
                    current_dir.append(directory)

        print("/" + "/".join(current_dir))
    return 0


def part2():
    return 0
