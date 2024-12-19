#Task: https://adventofcode.com/2024/day/18
f = open('y2024/data/day18.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]

#WIDTH=7
#HEIGHT=7
#TIME=12
WIDTH=71
HEIGHT=71
TIME=1024

def shortest_path(corrupted_bits):
    rows, cols = HEIGHT, WIDTH
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for y, x in corrupted_bits:
        grid[y][x] = 1  
    #for row in grid:
    #    print("".join("#" if cell == 1 else "." for cell in row))
    def is_valid(y, x):
        return 0 <= y < rows and 0 <= x < cols and grid[y][x] == 0

    queue = [(0, 0, 0)]  # (row, col, distance)
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[0][0] = True

    while queue:
        y, x, dist = queue.pop(0)
        #print(y, x, dist)

        if (y, x) == (rows - 1, cols - 1): # bottom-right corner
            return dist

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if is_valid(ny, nx) and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx, dist + 1))

    return -1  # no path exists

def part1():

    sum = 0
    corrupted_bits=[]
    for line in lines[:TIME]:
        x, y = [int(x) for x in line.split(",")]
        #print(x,y)
        corrupted_bits.append((y,x))
    
    '''grid = []
    for y in range(HEIGHT):
        g = ""
        for x in range(WIDTH):
            if(y,x) in corrupted_bits:
                g+="#"
                print("#",end="")
            else:
                g+="."
                print(".",end="")
        grid.append(g)
        print()
    print(grid)'''

    return shortest_path(corrupted_bits)


def part2():
    corrupted_bits=[]
    for line in lines:
        x, y = [int(x) for x in line.split(",")]
        #print(x,y)
        corrupted_bits.append((y,x))

    time = TIME
    passing = True
    while passing:
        time += 1
        if shortest_path(corrupted_bits[:time]) == -1:
            passing == False
            y, x = corrupted_bits[time-1]
            return str(x)+","+str(y)


if __name__ == "__main__":
    print()
    print("P1",part1()) # 248
    print("P2",part2()) # 32,55