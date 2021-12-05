# Task: https://adventofcode.com/2021/day/4
f = open('y2021/data/day4.txt', 'r')
lines = f.readlines()
f.close()


def is_this_bingo_bool(board):
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


def get_last_bingo_board(bingo_boards, bingo_boards_marks, numbers):
    boards_won = [False for _ in range(len(bingo_boards))]
    current_board = []
    current_board_marks = []
    current_number = 0

    for number in numbers:

        '''print("Number:", number)
        for board_id in range(len(bingo_boards)):
            for j in range(len(bingo_boards[0])):
                print(bingo_boards[board_id][j], bingo_boards_marks[board_id][j], sep="\t", end="\n")
            print()
        print()'''

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
                if is_this_bingo_bool(b_marks):
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
        get_last_bingo_board(bingo_boards, bingo_boards_marks, drawn_numbers)

    last_board_sum = 0
    for row in range(len(last_bingo_board)):
        for col in range(len(last_bingo_board[0])):
            if not last_bingo_marks[row][col]:
                last_board_sum += int(last_bingo_board[row][col])

    # print("---\n", last_board_sum, "*", last_bingo_number)
    return int(last_board_sum) * int(last_bingo_number)

# if you are reading this, I am so sorry for what I have done. Here is your reward for not running away:

# print(""" Merry christmas from rddrdhd ;)
# .      *    *           *.       *   .                      *     .
#                .   .                   __   *    .     * .     *
#     *       *         *   .     .    _|__|_        *    __   .       *
#   .  *  /\       /\          *        ('')    *       _|__|_     .
#        /  \   * /  \  *          .  <( . )> *  .       ('')   *   *
#   *    /  \     /  \   .   *       _(__.__)_  _   ,--<(  . )>  .    .
#       /    \   /    \          *   |       |  )),`   (   .  )     *
#    *   `||` ..  `||`   . *.   ... ==========='`   ... '--`-` ... *
# """)
