# Task: https://adventofcode.com/2021/day/21
f = open('y2021/data/day21.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]

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
    dice_rolls_count = 0
    while not won:
        for p in range(players):  # 2 players
            score = 0
            for _ in range(k_rolls):  # 3 rolls
                dice_rolls_count += 1
                dice_roll = dice_rolls_count % k_dice

                score += dice_roll
                board_pos[p] = (board_pos[p]+dice_roll) % k_board

            scores[p] += board_pos[p] if board_pos[p] != 0 else 10  # position 10 is [0] in array
            won = max(scores) >= winning_score
            if won:
                break
    return min(scores) * dice_rolls_count

def part2():
    return 0