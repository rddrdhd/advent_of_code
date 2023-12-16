#Task: https://adventofcode.com/2023/day/16
f = open('y2023/data/day16.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]

RIGHT= 0
DOWN = 1
LEFT = 2
UP = 3

class Contraption:
    def __init__(self, lines):
        self.rows = []
        for line in lines:
            self.rows.append(line)
        self.energized = []
        self.beams = []

    def get_reflection_direction(self, direction, char):
        if (direction == RIGHT and char == "/") or (direction == LEFT and char == "\\"):
            direction = UP
        elif (direction == RIGHT and char == "\\") or (direction == LEFT and char == "/"):
            direction = DOWN
        elif (direction == DOWN and char == "/") or direction == UP and char == "\\":
            direction = LEFT
        elif (direction == DOWN and char == "\\") or (direction == UP and char == "/"):
            direction = RIGHT
        return direction
    
    def print(self):
        print("")
        for y in range(len(self.rows)):
            for x in range(len(self.rows[0])):
                if (y,x) in self.energized:
                    print("#", end="")
                else:
                    print(self.rows[y][x],end="")
            print("")

    def shoot(self, y, x, direction, ttl = 100):
        ttl -= 1 # just in case, shouldn't matter

        # only if the ray was not fired this way yet
        if not [y, x, direction] in self.beams:
            # add ray fired
            self.beams.append([y, x , direction])
            
            # while in bounds of contraption
            while (ttl > 0 
                   and 0 <= y < len(self.rows) 
                   and 0 <= x < len(self.rows[0]) ):

                if (y, x) not in self.energized:
                    self.energized += [(y, x)]
                
                char = self.rows[y][x]

                if (char == "." 
                    or (direction in (LEFT, RIGHT) and char == "-") 
                    or (direction in (UP, DOWN) and char == "|")):
                    # do nothing
                    a=0
                   
                elif char in ("/","\\"): 
                    # mirror -> reflection
                    direction = self.get_reflection_direction(direction, char)

                else:  
                    # splitter -> refraction
                    if char == "-":
                        self.shoot(y, x-1, LEFT, ttl)
                        self.shoot(y, x+1, RIGHT, ttl)
                        return
                    else:
                        self.shoot(y-1, x, UP, ttl)
                        self.shoot(y+1, x, DOWN, ttl)
                        return
                    # shoot two
                if direction == RIGHT:
                    x+=1
                elif direction == DOWN:
                    y+=1
                elif direction == LEFT:
                    x-=1
                elif direction == UP:
                    y-=1
        return
    
def part1():
    c = Contraption(lines)
    c.shoot(0,0, RIGHT)
    return len(c.energized) # 6361

def part2():
    max_score = 0
    max_width = len(lines[0])
    max_height = len(lines)
    '''
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠰⢾⣶⣦⢀⣀⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣀⡀⢿⣿⡆⣿⣿⣿⣦⡀⠄⣀⣀⡀⠄⠄⠄⠄
    ⠄⠄⣰⣶⣄⠄⠄⠄⠄⠄⡾⠁⣀⠙⠸⣿⡇⡟⣋⣩⣴⣶⣶⣶⣍⢿⣷⣄⠄⠄
    ⠄⠄⠈⠙⠻⢷⡄⠄⠄⢠⣝⡀⠤⣴⣧⣭⠄⡞⠛⠻⣭⣭⣭⡛⢿⢸⣿⣿⡆⠄
    ⠄⠄⠄⠄⠄⠄⠑⠄⠄⠄⠙⠻⣿⣶⣶⣶⢸⠄⠒⠄⢸⣿⣿⣷⡌⡼⣿⣿⣧⠄
    ⣴⣿⣿⣿⣿⣷⣶⣤⣀⢠⣴⡾⢟⡻⢿⣿⣷⢄⣐⠶⠿⠿⠛⣛⣃⣴⣿⣿⡿⠄
    ⣿⠿⠛⠉⠉⢉⣉⡉⢭⣥⣿⣧⡘⣿⣮⣻⣿⣶⣮⣭⣍⣋⣭⣭⣴⣿⣿⣟⣱⣿
    ⠄⠄⠄⢀⣴⣿⠟⠄⠘⣿⡿⢛⣣⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⠄⠄⠄⠘⠻⠋⠄⠄⠄⠘⢇⣛⣛⣛⣩⣽⣿⣿⣿⣿⣿⣿⠋⣿⣿⣿⣿⣿⣿⣿
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⢏⣾⣿⣿⣿⣿⣿⣿⣿
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣤⣶⣶⣝⠻⢿⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⠿
    ⠄⠄⠄⠄⠄⠄⢀⣤⣾⣿⣿⣿⣿⣿⣿⣶⣬⣝⣛⡛⠿⠿⠿⠿⠿⢟⣛⣩⣤⣄                      
    '''
    for x, way in [(0, RIGHT), (max_width, LEFT)]:
        for y in range(len(lines)):
            c = Contraption(lines)
            c.shoot(y, x, way)
            score = len(c.energized)
            del c
            max_score = max(score, max_score)
    for y, way in [(0, DOWN),(max_height, UP)]:
        for x in range(len(lines[0])):
            c = Contraption(lines)
            c.shoot(y, x, way)
            score = len(c.energized)
            del c
            max_score = max(score, max_score)
    return max_score # 6701
