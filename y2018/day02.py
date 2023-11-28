#Task: https://adventofcode.com/2018/day/2
f = open('y2018/data/day02.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]

def part1():
    double_letter=0
    tripple_letter=0
    for line in lines:
        hist={}
        for char in line:
            if char in hist:
                hist[char]+=1
            else:
                hist[char]=1
        try:
            if list(hist.keys())[list(hist.values()).index(3)]:
                tripple_letter+=1
        except ValueError: # nothing tripple
            pass
        try:
            if list(hist.keys())[list(hist.values()).index(2)]:
                double_letter+=1
        except ValueError: # nothing double
            pass
    return double_letter*tripple_letter


def part2():
    return 0
