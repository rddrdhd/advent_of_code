# Task: https://adventofcode.com/2021/day/5

f = open('y2021/data/day05.txt', 'r')
lines = f.readlines()
f.close()

# array indexes for coordinates
X1 = 0
Y1 = 1
X2 = 2
Y2 = 3


def part1():
    # for diagram
    max_x = 0
    max_y = 0
    diagram = []

    # for coordinates
    values = []

    # parse lines into values
    for line in lines:
        numbers = line.replace(",", " ").replace(" -> ", " ")

        x1, y1, x2, y2 = map(int, numbers.split(" "))
        if x1 > max_x:
            max_x = x1
        if y1 > max_y:
            max_y = y1
        if x2 > max_x:
            max_x = x2
        if y2 > max_y:
            max_y = y2
        values.append([x1, y1, x2, y2])

    # fill 2D diagram with zeros
    for y in range(max_y + 1):
        diagram.append([0 for _ in range(max_x + 1)])

    # fill the diagram with values
    for value in values:  # for line
        if value[X1] == value[X2]:
            bigger_y = max(value[Y1], value[Y2])
            smaller_y = min(value[Y1], value[Y2])
            for y in range(smaller_y, bigger_y + 1):
                diagram[y][value[X1]] += 1
        if value[Y1] == value[Y2]:
            bigger_x = max(value[X1], value[X2])
            smaller_x = min(value[X1], value[X2])
            for x in range(smaller_x, bigger_x + 1):
                diagram[value[Y1]][x] += 1

    # sum the overlapping area
    sum = 0
    for line in diagram:
        for num in line:
            if num > 1:
                sum += 1

    return sum  # 7380


def part2():
    max_x = 0
    max_y = 0
    diagram = []
    values = []

    # parse data into values
    for line in lines:
        numbers = line.replace(",", " ").replace(" -> ", " ")

        x1, y1, x2, y2 = map(int, numbers.split(" "))

        max_x = max([x1, x2, max_x])
        max_y = max([y1, y2, max_y])

        values.append([x1, y1, x2, y2])

    # fill 2D diagram with zeros
    for y in range(max_y + 1):
        diagram.append([0 for _ in range(max_x + 1)])

    # fill the diagram with values
    for value in values:  # for line

        # add horizontal and vertical stuff
        if value[X1] == value[X2]:
            bigger_y = max(value[Y1], value[Y2])
            smaller_y = min(value[Y1], value[Y2])
            for y in range(smaller_y, bigger_y + 1):
                diagram[y][value[X1]] += 1
        elif value[Y1] == value[Y2]:
            bigger_x = max(value[X1], value[X2])
            smaller_x = min(value[X1], value[X2])
            for x in range(smaller_x, bigger_x + 1):
                diagram[value[Y1]][x] += 1

        # add diagonal stuff
        elif abs(value[X1]-value[X2]) == abs(value[Y1]-value[Y2]):

            # make all coordinates left->right
            if value[X1] > value[X2]:
                value[X1], value[X2] = value[X2], value[X1]
                value[Y1], value[Y2] = value[Y2], value[Y1]

            diagonal_length = value[X2] - value[X1]
            distance_range = range(abs(diagonal_length) + 1)

            if value[Y1] < value[Y2]:  # diagonal going down
                for d in distance_range:
                    diagram[value[Y1] + d][value[X1] + d] += 1
            else:  # diagonal going up
                for d in distance_range:
                    diagram[value[Y1] - d][value[X1] + d] += 1
        else:
            print("Error: The diagonal is not square")

    # sum the overlapping
    sum = 0
    for line in diagram:
        for num in line:
            if num > 1:
                sum += 1

    return sum  # 21373
