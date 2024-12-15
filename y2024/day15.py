#Task: https://adventofcode.com/2024/day/15
f = open('y2024/data/day15.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]

DIRECTIONS_MAP = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
BOX, ROBOT, WALL, BOX_LEFT, BOX_RIGHT, EMPTY  = "O", "@", "#", "[", "]", "."


def find_robot(room):
    for y in range(len(room)):
        for x in range(len(room[0])):
            if room[y][x] == ROBOT:
                return y, x
    return None


def calculate_score(room):
    total = 0
    for y in range(len(room)):
        for x in range(len(room[0])):
            if room[y][x] == BOX_LEFT or room[y][x] == BOX:
                total += 100*y + x
    return total


def print_room(move, room):
    print("Move", move + ":")
    for y in range(len(room)):
        for x in range(len(room[0])):
            print(room[y][x],end="")
        print()    


def can_move(room, to_move, dy, dx):
    for y, x in to_move:
        ny, nx = y + dy, x + dx
        if (ny, nx) not in to_move:
            if room[ny][nx] == WALL: 
                return False
            elif room[ny][nx] == BOX: # for part 1
                to_move.append((ny, nx))
            elif room[ny][nx] == BOX_LEFT: # for part 2
                to_move.extend([(ny, nx), (ny, nx+1)])
            if room[ny][nx] == BOX_RIGHT: # for part 2
                to_move.extend([(ny, nx), (ny, nx-1)])
    return True


def do_the_move(room, to_move, dy, dx):
    for y, x in reversed(to_move): # move one by one from the end
        room[y + dy][x + dx], room[y][x] = room[y][x], room[y + dy][x + dx]  


def solve(part_two=False, visual=False):
    room, moves = ("\n".join(lines)).split("\n\n")
    moves = moves.replace("\n", "")

    if part_two == True:
        room = room.replace(WALL, 2 * WALL)
        room = room.replace(EMPTY, 2 * EMPTY)
        room = room.replace(BOX, BOX_LEFT + BOX_RIGHT)
        room = room.replace(ROBOT, ROBOT + EMPTY)

    room = [list(y) for y in room.split("\n")] 
    y, x = find_robot(room)

    for move in moves:
        dy, dx = DIRECTIONS_MAP[move]
        to_move = [(y, x)]

        if can_move(room, to_move, dy, dx):
            do_the_move(room, to_move, dy, dx)
            y, x = y + dy, x + dx

        if visual:
            print_room(move, room)
    return calculate_score(room)

    
def part1(visual=False):
    return solve(part_two=False, visual=visual)


def part2(visual=False):
    return solve(part_two=True, visual=visual)


if __name__ == "__main__":
    print()
    print("P1",part1()) # 1446158
    print("P2",part2()) # 1446175