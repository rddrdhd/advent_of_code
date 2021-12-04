# Task: https://adventofcode.com/2021/day/4

f = open('y2021/data/day4.txt', 'r')
lines = f.readlines()
f.close()


def is_this_bingo(board, number):
    # check bingos
    for line in board:
        if line == ['X', 'X', 'X', 'X', 'X']:
            # print("ROW BINGO")
            return board, number

    for column in range(len(board[0])):
        bing_col = []
        for line in board:
            bing_col.append(line[column])
        if bing_col == ['X', 'X', 'X', 'X', 'X']:
            # print("COL BINGO")
            return board, number


def get_first_bingo_board(bingo_boards, numbers):
    for number in numbers:
        for board in bingo_boards:
            # mark numbers
            for l, line in enumerate(board):
                if number in line:
                    line = ["X" if x == number else x for x in line]  # replace number with X
                    board[l] = line
        for b, board in enumerate(bingo_boards):
            if is_this_bingo(board, number):
                return board, number


def part1():
    drawn_numbers = lines[0].strip().split(",")
    bingo_boards = []
    bingo_board = []
    for i in range(2, len(lines)):
        # filter empty splits from numbers with spaces
        bingo_line = list(filter(None, lines[i].strip().split(" ")))

        # empty array is from "\n\n" in input. I had to add two newlines at the end of the .txt file.
        if len(lines[i].strip()) == 0:
            bingo_boards.append(bingo_board)
            bingo_board = []
        else:
            bingo_board.append(bingo_line)

    winner_board, winner_number = get_first_bingo_board(bingo_boards, drawn_numbers)

    winner_board_sum = 0
    for row in winner_board:
        for col in row:
            if col != 'X':
                winner_board_sum += int(col)

    return int(winner_board_sum) * int(winner_number)
