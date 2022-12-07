# Task: https://adventofcode.com/2022/day/7
f = open('y2022/data/day07.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]


def get_locations():
    current_dir = []  # empty means /
    locations = {"/": 0}
    location = "/" + "/".join(current_dir)
    for line in lines:
        if line == '$ ls':
            continue
        elif line == '$ cd /':
            current_dir = []
        elif " cd " in line:
            directory = line[5:]
            if directory == "..":
                current_dir.pop()
            else:
                current_dir.append(directory)
        location = "/" + "/".join(current_dir)
        if locations.get(location) is None:
            locations[location] = 0

        if line[0] != "$":
            try:
                locations[location] += int(line.split(" ")[0])
            except ValueError:
                continue

    # sum subdirectory sizes
    for key, size in locations.items():
        for key2, size2 in locations.items():
            if key != key2 and key in key2:
                locations[key] += size2
    return locations


def part1():
    locations = get_locations()
    total = 0
    # sum for the result
    for location, size in locations.items():
        if size < 100000:
            total += size
    return total


def part2():
    locations = get_locations()
    total_space = 70000000
    free_goal = 30000000
    root_size = locations["/"]
    final_dir = ["/", root_size] # i want to find smaller than root dir
    for directory, size in locations.items():
        free_space = total_space - root_size + size
        if free_space >= free_goal:
            if total_space - root_size + final_dir[1] > free_space:
                final_dir = [directory, size]

    return final_dir[1]
