# Task: https://adventofcode.com/2021/day/1
#Load lines
file = open('day1_data.txt', 'r')
Lines = file.readlines()
file.close()


def part1():
    count = 0
    last_line = ""

    for line in Lines:
        current_line = int(line.strip())
        if last_line != "":
            if last_line < current_line:
                count+=1
        last_line = current_line

    return count # 1715


def part2():
    count = 0
    window_size = 3
    last_window = []
    current_window = []

    for i in range( 0, len(Lines)-(window_size) ): # range(0,2000-3)
        current_window = [int(Lines[i]),int(Lines[i+1]),int(Lines[i+2])]
        if(sum(current_window) > sum(last_window)):
            count+=1

        last_window = current_window

    return count # 1739

