# Task: https://adventofcode.com/2022/day/2
f = open('y2022/data/day02.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]


# A == X = Kamen (1 p)
# B == Y = Papir (2p)
# C == Z = Nuzky (3p)
def part1():
    score = 0
    for line in lines:
        round_score = 0
        first, second = (line.split())

        second_won = (first == "A" and second == "Y") or (first == "B" and second == "Z") or (
                first == "C" and second == "X")
        first_won = (first == "A" and second == "Z") or (first == "B" and second == "X") or (
                first == "C" and second == "Y")
        if first_won:
            round_score += 0
        elif second_won:
            round_score += 6
        else:
            round_score += 3
        if second == "X":
            round_score += 1
        if second == "Y":
            round_score += 2
        if second == "Z":
            round_score += 3
        score += round_score
    return score


# A = Kamen (1 p)
# B = Papir (2p)
# C = Nuzky (3p)
# X == loose
# Y == draw
# Z == win

# WIP:
def part2():
    score = 0
    kamen = "A"
    nuzky = "B"
    papir = "C"
    prohra = "X"
    remiza = "Y"
    vyhra = "Z"
    for line in lines:
        round_score = 0
        opponent, result = (line.split())
        if result == vyhra: round_score += 6
        if result == remiza: round_score += 3
        i_play_stone = (opponent == kamen and result == remiza) or (opponent == nuzky and result == vyhra) or (
                opponent == papir and result == prohra)
        i_play_scissors = (opponent == nuzky and result == remiza) or (opponent == papir and result == vyhra) or (
                opponent == kamen and result == prohra)

        if i_play_stone:
            round_score += 1
        elif i_play_scissors:
            round_score += 3
        else: #i_play_paper
            round_score += 2
        score += round_score
        print(round_score)

    return score  # 4098 too low,  11958 too low
