# Task: https://adventofcode.com/2022/day/1
f = open('y2022/data/day14.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]


class Map:
    stones = []
    lying_sand = []
    sand_falling_from = [0, 500]

    def fill_stones(self):
        for line in lines:
            numbers = line.split(" -> ")
            l = []
            for i, number in enumerate(numbers):
                x, y = number.split(",")  # big/small
                x, y = int(x), int(y)
                self.stones.append([y, x])
                if i != 0:
                    last_x, last_y = l[1], l[0]
                    if last_y == y:  # if same y (small)
                        if x + 1 > last_x:
                            r = range(last_x, x)
                        else:
                            r = range(x, last_x)

                        for new_x in r:
                            stone = [y, new_x]
                            if stone not in self.stones:
                                self.stones.append(stone)

                    if last_x == x:  # if same x (big)
                        if y + 1 > last_y:
                            r = range(last_y, y)
                        else:
                            r = range(y, last_y)

                        for new_y in r:
                            stone = [new_y, x]
                            if stone not in self.stones:
                                self.stones.append(stone)

                l = [int(y), int(x)]

    def add_end(self):
        xs = [i[1] for i in self.stones]
        left_x = min(xs)
        right_x = max(xs)

        floor_y = max([i[0] for i in self.stones])+2

        for x in range(left_x-20, right_x+20):
            self.stones.append([floor_y, x])


    def sand_flood(self, endless_void = True):
        sand_y, sand_x = self.sand_falling_from
        floor_y = max([i[0] for i in self.stones])

        if not endless_void:
            self.add_end()

        while True:
            sand_fell = True
            for dir_y, dir_x in [[1, 0], [1, -1], [1, 1]]:
                if [sand_y + dir_y, sand_x + dir_x] not in (self.stones + self.lying_sand):
                    sand_x += dir_x
                    sand_y += dir_y
                    sand_fell = False
                    break
            if sand_y > floor_y and endless_void:
                break
            if sand_fell:
                self.lying_sand.append([sand_y, sand_x])
                if [sand_y, sand_x] == self.sand_falling_from:
                    break
                sand_y, sand_x = self.sand_falling_from

    def print_map(self, y_range=range(-2, 12), x_range=range(492, 530)):
        xs = [i[1] for i in self.stones]
        left_x = min(xs)
        right_x = max(xs)

        floor_y = max([i[0] for i in self.stones]) + 2

        y_range = range(0, floor_y)
        x_range = range(left_x, right_x)
        for y in y_range:
            print("\n", end="")
            for x in x_range:
                if [y, x] in self.stones:
                    print("#", end="")
                elif [y, x] == self.sand_falling_from:
                    print("+", end="")
                elif [y, x] in self.lying_sand:
                    print("O", end="")
                else:
                    print(".", end="")


def part1():
    m = Map()
    m.fill_stones()
    m.sand_flood(True)

    m.print_map()
    return len(m.lying_sand)


def part2():
    m = Map()
    m.fill_stones()
    m.sand_flood(False)

    m.print_map()
    return len(m.lying_sand)



def part2():
    return 0
