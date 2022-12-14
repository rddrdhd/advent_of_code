# Task: https://adventofcode.com/2022/day/1
f = open('y2022/data/day14.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]


class Map:
    stones = []
    lying_sand = []
    sand_falling_from = [500,0]

    def fill_map(self):
        for line in lines:
            numbers = line.split(" -> ")
            l = []
            for i, number in enumerate(numbers):
                y, x = number.split(",")
                l.append([int(y), int(x)])
                if i != 0:
                    if l[i - 1][0] == l[i][0]:
                        for z in range(l[i - 1][1], l[i][1]):
                            l.append([y, z])
                    if l[i - 1][1] == l[i][1]:
                        for z in range(l[i - 1][0], l[i][0]):
                            l.append([z, x])
            self.stones += l


def part1():
    m = Map()
    m.fill_map()
    return 0


def part2():
    return 0
