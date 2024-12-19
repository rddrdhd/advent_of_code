import heapq

f = open('y2024/data/day16.txt', 'r')
lines = f.readlines()
f.close()

DIRECTIONS = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
WIDTH, HEIGHT = len(lines[0]), len(lines)
START, END, WALL = 'S', 'E', '#'

def parse_grid():
    start, end = None, None
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if lines[y][x] == START:
                start = (y, x)
            elif lines[y][x] == END:
                end = (y, x)
    return start, end


def solve(part_two=False):
    start, end = parse_grid()
    priority_queue = [(0, start[0], start[1], END, set())]  # (cost, y, x, direction, path_set)
    visited = {}
    best_cost = float('inf')
    best_tiles = set()

    while priority_queue:
        cost, y, x, dir, path_set = heapq.heappop(priority_queue)

        if not part_two and (y, x) == end:
            return cost
        elif part_two:
            if cost > best_cost:
                continue
            elif (y, x) == end:
                if cost < best_cost:
                    best_cost = cost
                    best_tiles = path_set.union({(y, x)})
                elif cost == best_cost:
                    best_tiles.update(path_set.union({(y, x)}))
                continue

        if (y, x, dir) in visited and visited[(y, x, dir)] < cost:
            continue

        visited[(y, x, dir)] = cost

        for new_dir, (dy, dx) in DIRECTIONS.items():
            ny, nx = y + dy, x + dx
            if 0 <= ny < HEIGHT and 0 <= nx < WIDTH and lines[ny][nx] != WALL:
                if part_two:
                    new_path_set = new_path_set = path_set.union({(y, x)})
                else:
                    new_path_set = None

                new_cost = cost + 1
                new_cost += 1000 if new_dir != dir else 0

                heapq.heappush(priority_queue, (new_cost, ny, nx, new_dir, new_path_set))

    # part 2 return the number of tiles in the best paths
    if part_two:
        return len(best_tiles)
    return None  # part 1 if no path is found

def part1():
    return solve()


def part2():
    return solve(part_two=True)


if __name__ == "__main__":
    print("P1", part1())  # 88416
    print("P2", part2())  # 442
