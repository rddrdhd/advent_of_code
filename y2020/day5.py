# Task: https://adventofcode.com/2020/day/5

f = open('y2020/data/day5.txt', 'r')
lines = f.readlines()
f.close()


def get_half(command_bit, seat_ids):
    if len(seat_ids) == 1:
        return seat_ids
    if command_bit == "B" or command_bit == "R":
        return seat_ids[len(seat_ids) // 2:]
    if command_bit == "F" or command_bit == "L":
        return seat_ids[:len(seat_ids) // 2]


def get_seat_id(commands, last_row_number, number_of_columns):
    commands = commands.strip()

    seat_ids = [x for x in range(0, last_row_number)]
    for command_bit in commands[:-3]:
        seat_ids = get_half(command_bit, seat_ids)
    seat_row = seat_ids[0]

    seat_columns = [x for x in range(0, number_of_columns)]  # define columns
    for command_bit in commands[-3:]:
        seat_columns = get_half(command_bit, seat_columns)
    seat_column = seat_columns[0]

    seat_id = seat_row * number_of_columns + seat_column
    return seat_id


def part1():
    last_row_number = 128
    last_column_number = 8
    seat_ids = [x for x in range(last_row_number)]
    new_seat_ids = seat_ids.copy()

    for command_line in lines:
        new_seat_ids.append(get_seat_id(command_line, last_row_number, last_column_number))
    return max(new_seat_ids)  # 883


def part2():
    return 0
