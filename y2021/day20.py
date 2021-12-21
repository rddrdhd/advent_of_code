# Task: https://adventofcode.com/2021/day/20
f = open('y2021/data/day20.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]
P1 = 0
P2 = 1
def get_starting_pos(lines):
    return [int(s[-1]) for s in lines]

def part1():
    winning_score = 1000
    k_dice = 100
    k_board = 10
    k_rolls = 3
    players = 2
    scores = [0 for _ in range(players)]

    board_pos = get_starting_pos(lines)
    won = False
    dice_roll = 0 # just init, for value
    dice_rolls_count = 0
    while not won:
        for p in range(players):  # 2 players
            score = 0
            for _ in range(k_rolls):  # 3 rolls
                dice_rolls_count += 1
                score += dice_roll
                dice_roll = ((dice_roll) % (k_dice))+1

                board_pos[p] = ((board_pos[p]+dice_roll) % k_board)

            scores[p] += board_pos[p] if board_pos[p] != 0 else 10
            won = max(scores) >= winning_score
            if (won):
                break
    return min(scores)*dice_rolls_count

def part2():
    return 0