#Task: https://adventofcode.com/2024/day/14
import time
f = open('y2024/data/day14.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]

TEST_SIZE = (11,7)
PROD_SIZE = (101,103)


def part1(num_of_s=100, visual=False):
    size = PROD_SIZE
    robots = []
    quadrants = [0, 0, 0, 0]
    for line in lines:
        _, pos, vel = line.split("=")
        position = [int(p.strip()) for p in pos[:-2].split(",")]
        velocity = [int(p.strip()) for p in vel.split(",")]

        for s in range(num_of_s):
            position[0] = (position[0] + velocity[0]) % size[0]
            position[1] = (position[1] + velocity[1]) % size[1]

        px, py = position
        robots.append((px, py))

        if 0 <= px < size[0] // 2 and 0 <= py < size[1] // 2:
            quadrants[0] += 1
        elif 0 <= px < size[0] // 2 and size[1] // 2 < py < size[1]:
            quadrants[1] += 1
        elif size[0] // 2 < px < size[0] and 0 <= py < size[1] // 2:
            quadrants[2] += 1
        elif size[0] // 2 < px < size[0] and size[1] // 2 < py < size[1]:
            quadrants[3] += 1
            
    if visual:
        for y in range(size[1]):
            for x in range(size[0]):
                if (x,y) in robots:
                    print("X",end="")
                else:
                    print(".",end="")
            print("")
    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def part2():
    num_of_s =0
    while True:
        if (num_of_s - 28) % 101 == 0 and (num_of_s - 84) % 103==0:
            return num_of_s
        num_of_s+=1



if __name__ == "__main__":
    print()
    print("P1",part1()) # 224438715
    print("P2",part2()) # 7603

    # change this to test the visuals. Comment the inner "if" to go second-by-second.
    if False:
        ''' While going through this loop, I noticed every ~ 100 seconds there is formed a big column/row, 
        so I noted the numbers and found out its repeating after 101 and 103 seconds each.
        First I noticed the columns so I checked if (num_of_s - 28) % 101 == 0 is always this column and that worked. 
        Then I realized I was the row too, so I went second by second again to discover that it's whenever (num_of_s - 84) % 103==0.
        Works only with a real input, not the testing one.'''
        
        num_of_s =0
        while True:
            if (num_of_s - 28) % 101 == 0 or (num_of_s - 84) % 103==0:
                print(num_of_s)
                part1(num_of_s, True)
                input("Press Enter to continue...")
            num_of_s+=1