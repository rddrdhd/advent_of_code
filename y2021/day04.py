# Task: https://adventofcode.com/2021/day/4

f = open('y2021/data/day04.txt', 'r')
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

def is_this_bingo_bool2(board):
    for line in board:
        if line == [True, True, True, True, True]:
            return True

    for column in range(len(board[0])):
        bingo_col = []
        for line in board:
            bingo_col.append(line[column])
        if bingo_col == [True, True, True, True, True]:
            return True

    return False


def get_last_bingo_board2(bingo_boards, bingo_boards_marks, numbers):
    boards_won = [False for _ in range(len(bingo_boards))]
    current_board = []
    current_board_marks = []
    current_number = 0

    for number in numbers:
        # for each board marks
        for board_id, board_marks in enumerate(bingo_boards_marks):
            # get board status
            board_won = boards_won[board_id]
            if not board_won:
                current_board = bingo_boards[board_id]
                current_board_marks = bingo_boards_marks[board_id]
                current_number = number

                # mark the number
                for th_line, line_mark in enumerate(board_marks):
                    for th_mark in range(len(bingo_boards_marks[board_id][th_line])):
                        if number == bingo_boards[board_id][th_line][th_mark]:
                            bingo_boards_marks[board_id][th_line][th_mark] = True

            for b_id, b_marks in enumerate(bingo_boards_marks):
                # BINGO
                if is_this_bingo_bool2(b_marks):
                    boards_won[b_id] = True
                    if False not in boards_won:
                        return current_board, current_board_marks, current_number


def part2():
    drawn_numbers = lines[0].strip().split(",")
    bingo_boards_marks = []
    bingo_board_marks = []
    bingo_boards = []
    bingo_board = []
    for i in range(2, len(lines)):
        bingo_line = list(filter(None, lines[i].strip().split(" ")))
        bingo_marks_line = [False for _ in range(len(bingo_line))]

        if len(lines[i].strip()):
            bingo_board.append(bingo_line)
            bingo_board_marks.append(bingo_marks_line)
        else:
            # I had to add two newlines at the end of the .txt file.
            bingo_boards.append(bingo_board)
            bingo_board = []
            bingo_boards_marks.append(bingo_board_marks)
            bingo_board_marks = []

    last_bingo_board, last_bingo_marks, last_bingo_number = \
        get_last_bingo_board2(bingo_boards, bingo_boards_marks, drawn_numbers)

    last_board_sum = 0
    for row in range(len(last_bingo_board)):
        for col in range(len(last_bingo_board[0])):
            if not last_bingo_marks[row][col]:
                last_board_sum += int(last_bingo_board[row][col])

    # print("---\n", last_board_sum, "*", last_bingo_number)
    return int(last_board_sum) * int(last_bingo_number)

# if you are reading this, I am so sorry for what I have done. Here is your reward:

# .      *    *           *.       *   .                      *     .
#                .   .                   __   *    .     * .     *
#     *       *         *   .     .    _|__|_        *    __   .       *
#   .  *  /\       /\          *        ('')    *       _|__|_     .
#        /  \   * /  \  *          .  <( . )> *  .       ('')   *   *
#   *    /  \     /  \   .   *       _(__.__)_  _   ,--<(  . )>  .    .
#       /    \   /    \          *   |       |  )),`   (   .  )     *
#    *   `||` ..  `||`   . *.   ... ==========='`   ... '--`-` ... *
#
