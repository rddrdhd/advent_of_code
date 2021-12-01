# Task: https://adventofcode.com/2021/day/1

f = open('y2021/data/day1.txt', 'r')
lines = f.readlines()
f.close()

def part1():
    count = 0
    last_line = ""

    for line in lines:
        current_line = int(line.strip())
        if last_line != "":
            if last_line < current_line:
                count+=1
        last_line = current_line

    return count # 1715


def part2():
    count = 0
    last_sum = 0

    window_size = 3
    current_window = []

    for i in range( 0, len(lines)-(window_size) ): # range(0,2000-3)
        current_window = [  int(lines[i+0]),
                            int(lines[i+1]),
                            int(lines[i+2]),  ]
        if(sum(current_window) > last_sum):
            count+=1

        last_sum = sum(current_window)

    return count # 1739
