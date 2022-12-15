import re

f = open('y2022/data/day15.txt', 'r')
lines = f.readlines()
f.close()
lines = [l.strip() for l in lines]


class Map:
    sensors = []
    beacons = []
    empty = []
    reaches = []
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0

    def __init__(self, lines):
        for line in lines:
            sx, sy, bx, by = [int(j) for j in re.findall(r'\d+', line)]
            self.sensors.append([int(sy), int(sx)])
            self.beacons.append([int(by), int(bx)])
            self.reaches.append(int(abs(sy - by) + abs(sx - bx)))
        self.min_x = min(i[1] for i in self.beacons + self.sensors) - max(self.reaches)
        self.max_x = max(i[1] for i in self.beacons + self.sensors) + max(self.reaches)
        self.min_y = min(i[0] for i in self.beacons + self.sensors) - max(self.reaches)
        self.max_y = max(i[0] for i in self.beacons + self.sensors) + max(self.reaches)

    def fill_empty(self):
        for i in range(len(self.sensors)):
            print(self.reaches)
            print(self.reaches[i])

            for y in range(0, self.reaches[i] + 1):
                for x in range(0, self.reaches[i] + 1):
                    if x + y <= self.reaches[i]:
                        a = [self.sensors[i][0] + y, self.sensors[i][1] + x]
                        b = [self.sensors[i][0] - y, self.sensors[i][1] - x]
                        c = [self.sensors[i][0] + y, self.sensors[i][1] - x]
                        d = [self.sensors[i][0] - y, self.sensors[i][1] + x]
                        for e in a, b, c, d:
                            if e not in self.empty:
                                self.empty.append(e)

    def print(self):
        print(self.sensors)
        print(self.beacons)

        for y in range(self.min_y, self.max_y):
            print(y, end="\t")
            for x in range(self.min_x, self.max_x):
                if [y, x] in self.beacons:
                    ch = "B"
                elif [y, x] in self.sensors:
                    ch = "S"
                elif [y, x] in self.empty:
                    ch = "#"
                else:
                    ch = "."
                print(ch, end="")
            print()

    def get_not_beacon_spots(self, row):
        count = 0
        for e in self.empty:
            if e[0] == row and e not in self.beacons and e not in self.sensors:
                count += 1
                print(e)
        return count

   

def pokus_2(lines, main_y=10):
    the_xs = []
    occupied_xs = []
    for line in lines:
        sx, sy, bx, by = [int(j) for j in re.findall(r'\d+', line)]

        if by == main_y:
            occupied_xs.append(bx)
            if bx in the_xs:
                the_xs.remove(bx)
        if sy == main_y:
            if sx in the_xs:
                the_xs.remove(sx)
            occupied_xs.append(sx)
        reach = int(abs(sy - by) + abs(sx - bx))

        if main_y in range(sy - reach, sy + reach):
            # how far is that? according to that shrink the row range
            how_far = abs(main_y - sy)
            for i in range((sx - reach) + how_far, (sx + reach + 1) - how_far):
                if i not in the_xs and i not in occupied_xs:
                    the_xs.append(i)
    return len(the_xs)

def part1():
    #TODO: make it... not O(x^x^x^x^x^x^x^x...)
    #m = Map(lines)
    #m.fill_empty()
    #m.print()
    return pokus2(lines, 2000000)
    #return m.get_not_beacon_spots(10)
    # return m.get_not_beacon_spots(2000000)


def part2():
    return 0
