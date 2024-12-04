#Task: https://adventofcode.com/2024/day/4
f = open('y2024/data/day04.txt', 'r')
lines = f.readlines()
f.close()

Y, X = 0,1
N = (-1,0)
S = (1,0)
W = (0,-1)
E = (0 ,1)
NE = (-1,1)
NW = (-1,-1)
SE = (1,1)
SW = (1,-1) 

DIRECTIONS = [N, S, W, E, NE, NW, SE, SW]

lines = [s.strip() for s in lines]


def is_in_bounds(y, x):
    return 0 <= y < len(lines) and 0 <= x < len(lines[0])


def part1():
    total = 0
    xs = []

    # Find all 'X' positions
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == 'X':
                xs.append((i, j))  # Store the position of 'X'

    # Check for "XMAS" in all directions
    for x in xs:
        for d in DIRECTIONS:
            word_found = True
            for i, l in enumerate(['X', 'M', 'A', 'S']):
                c_y = x[Y] + d[Y]*i  # Row index
                c_x = x[X] + d[X]*i  # Column index

                if not is_in_bounds(c_y, c_x):
                    word_found = False
                    break

                # Check if the letter matches
                if lines[c_y][c_x] != l:
                    word_found = False
                    break

            if word_found:
                total += 1

    return total # 2642



def part2():
    sum = 0
    ass = [] # hahahaha
    
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == 'A':
                ass.append((i, j)) 

    for a in ass:
        mask_passing = True
        
        # both diagonals positions
        ne_pos = (a[Y] + NE[Y], a[X] + NE[X])
        nw_pos = (a[Y] + NW[Y], a[X] + NW[X])
        se_pos = (a[Y] + SE[Y], a[X] + SE[X])
        sw_pos = (a[Y] + SW[Y], a[X] + SW[X])

        if all(is_in_bounds(pos[Y],pos[X]) for pos in [ne_pos, nw_pos, se_pos, sw_pos]):
            ne = lines[ne_pos[Y]][ne_pos[X]]
            nw = lines[nw_pos[Y]][nw_pos[X]]
            se = lines[se_pos[Y]][se_pos[X]]
            sw = lines[sw_pos[Y]][sw_pos[X]]
            
            # MAS or SAM in both diagonals
            if not (((ne == "M" and sw == "S") or (ne == "S" and sw == "M")) and \
               ((nw == "M" and se == "S") or (nw == "S" and se == "M"))):
                mask_passing = False
        else:
            mask_passing = False
        
        if mask_passing:
            sum += 1
    return sum # 1974


if __name__ == "__main__":
    print()
    print("P1",part1())
    print("P2",part2())