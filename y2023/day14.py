#Task: https://adventofcode.com/2023/day/14
f = open('y2023/data/day14.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]
  
Y = 0
X = 1

NORTH = 0
WEST = 1
SOUTH = 2
EAST = 3
class Platform:
    def __init__(self, lines):
        self.rows = lines
        self.width = len(lines[0])
        self.height = len(lines)
        self.rocks_round = []
        self.rocks_round_fixed = []
        self.rocks_cubes = []
        self.fixed_for = None
        self.new_rock_places = []
        for y in range(self.height):
            for x in range(self.width):
                if self.rows[y][x] == "O":
                    self.rocks_round.append((y, x))
                elif self.rows[y][x] == "#":
                    self.rocks_cubes.append((y, x))

    def reset(self):
        self.rocks_round += sorted(list(set(self.rocks_round_fixed)))
        self.rocks_round_fixed = []
        self.new_rock_places = []

    def move_a_step(self, way=NORTH):
        self.new_rock_places = []
        if way in [NORTH, EAST]:
            i = 0
            # go through all the rocks from left to right/up to down
            while i < len(self.rocks_round):
                rock = self.rocks_round[i]
                if way == NORTH:
                    if rock[Y] <= 0 or (rock[Y]-1,rock[X]) in self.rocks_round_fixed + self.rocks_cubes:
                        self.rocks_round_fixed.append(self.rocks_round[i])
                    else:
                        self.new_rock_places.append((rock[Y]-1,rock[X]))
                
                elif way == WEST:
                        if rock[X] <= 0 or (rock[Y],rock[X]-1) in self.rocks_round_fixed + self.rocks_cubes:
                            self.rocks_round_fixed.append(self.rocks_round[i])
                        else:
                            self.new_rock_places.append((rock[Y],rock[X]-1))
                i+= 1

        else:
            i = len(self.rocks_round)-1
            # go through all the rocks from right to left/down to up
            while i > 0:
                rock = self.rocks_round[i]
                if way == EAST:
                    if rock[X] >= self.width-1 or (rock[Y],rock[X]+1) in self.rocks_round_fixed + self.rocks_cubes:
                        self.rocks_round_fixed.append(self.rocks_round[i])
                    else:
                        self.new_rock_places.append((rock[Y],rock[X]+1))
                elif way == SOUTH:
                    print(rock,end="->")
                    if rock[Y] >= self.height-1 or (rock[Y]+1,rock[X]) in self.rocks_round_fixed + self.rocks_cubes:
                        self.rocks_round_fixed.append(self.rocks_round[i])
                        print("STUCKED")
                    else:
                        self.new_rock_places.append((rock[Y]+1,rock[X]))
                        print("MOVE")
                i-=1
        self.rocks_round = sorted(list(set(self.new_rock_places)))


    def tilt(self, way=NORTH):
        while len(self.rocks_round):
            self.move_a_step(way)
        self.reset()   


    def print(self):
        print("")
        for y in range(self.height):
            for x in range(self.width):
                if (y,x) in self.rocks_round_fixed:
                    print("0",end="")
                elif (y,x) in  self.rocks_round:
                    print("O",end="")
                elif(y,x) in self.rocks_cubes:
                    print("#",end="")
                else:
                    print(".",end="")
            print("")
        print(len(self.rocks_round))


    def get_score(self):
        sum = 0
        for rock in self.rocks_round_fixed+self.rocks_round:
            row_score = self.height-rock[Y]
            sum += row_score
        return sum
        
def part1():
    a = Platform(lines)
    a.tilt(NORTH)
    return a.get_score()
  
def part2():
    return None