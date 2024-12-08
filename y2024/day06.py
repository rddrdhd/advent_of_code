#Task: https://adventofcode.com/2024/day/6
f = open('y2024/data/day06.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]
import re

# Directions
N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)
DIRECTIONS = [N, E, S, W] # ^>v<


def parse_input():
    obstacles = set()
    guard_pos = None
    guard_is_facing = None

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                obstacles.add((y, x))
            elif char in "^>v<":
                guard_pos = (y, x)
                guard_is_facing = "^>v<".index(char)

    return guard_pos, guard_is_facing, obstacles


def get_visited_points():
    guard_pos, guard_is_facing, obstacles = parse_input()
    visited_states = {d: [] for d in DIRECTIONS}
    visited_states[DIRECTIONS[guard_is_facing]].append(guard_pos)

    starting_guard_pos = guard_pos
    starting_pos_encountered = 1

    while True:
        new_y = guard_pos[0] + DIRECTIONS[guard_is_facing][0]
        new_x = guard_pos[1] + DIRECTIONS[guard_is_facing][1]
        new_pos = (new_y, new_x)

        in_bounds = 0 <= new_y < len(lines) and 0 <= new_x < len(lines[0])
        no_obstacle = new_pos not in obstacles
        circling = new_pos in visited_states[DIRECTIONS[guard_is_facing]]

        if circling or not in_bounds:
            break
        if no_obstacle:
            guard_pos = new_pos
        else:
            guard_is_facing = (guard_is_facing + 1) % 4

        visited_states[DIRECTIONS[guard_is_facing]].append(guard_pos)
        if guard_pos == starting_guard_pos:
            starting_pos_encountered += 1

    all_positions = []
    for positions in visited_states.values():
        for pos in positions:
            all_positions.append(pos)

    return set(all_positions)


def part1():
    return len(get_visited_points())


def part2():
    initial_guard_pos, initial_guard_is_facing, initial_obstacles = parse_input()
    original_path = get_visited_points() # only on guard's original path

    ended_cycling = 0
    for y, x in original_path: 
        # Reset obstacles, guard and visited positions
        obstacles = initial_obstacles.copy()
        guard_pos = initial_guard_pos
        guard_is_facing = initial_guard_is_facing
        visited_states = {d: [] for d in range(len(DIRECTIONS))}

        # new obstacle
        obstacles.add((y,x))

        while True:
            new_y = guard_pos[0] + DIRECTIONS[guard_is_facing][0]
            new_x = guard_pos[1] + DIRECTIONS[guard_is_facing][1]
            new_pos = (new_y, new_x)

            in_bounds = 0 <= new_y < len(lines) and 0 <= new_x < len(lines[0])
            circling = new_pos in visited_states[guard_is_facing]

            if circling:
                ended_cycling += 1
                break
            if not in_bounds:
                break
            if new_pos not in obstacles:
                guard_pos = new_pos
            else:
                guard_is_facing = (guard_is_facing + 1) % 4 # turn right

            visited_states[guard_is_facing].append(guard_pos)

    return ended_cycling


if __name__ == "__main__":
    print()
    print("P1",part1()) # 5199
    print("P2",part2()) # 1915