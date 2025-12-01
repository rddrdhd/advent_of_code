#Task: https://adventofcode.com/2025/day/1
f = open('y2025/data/day01.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]


def part1():
    num = 50
    sum = 0
    for line in lines:
        dir, steps = line[0], int(line[1:])
        if dir == "R": 
            num += steps
        else: 
            num -= steps
        num = num % 100
        if num == 0: 
            sum+=1
    return sum


def part2():
    num = 50
    sum = 0
    for line in lines:
        dir, steps = line[0], int(line[1:])
        prev_num = num
        if dir == "R": 
            num += steps
            sum += num//100 - prev_num//100
        else: 
            num -= steps
            sum += (prev_num-1)//100 - (num-1)//100
        num = num % 100
    return sum

if __name__ == "__main__":
    print()
    print("P1",part1())
    print("P2",part2())