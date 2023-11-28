#Task: https://adventofcode.com/2028/day/1
f = open('y2018/data/day01.txt', 'r')
lines = f.readlines()
f.close()
lines = [int(eval(s.strip())) for s in lines]

def part1():
    res=0
    for num in lines:
        res+=num
    return res

def part2():
    i = 0
    freq = 0
    found = False
    reached = [freq]
    size = len(lines)
    while not found and i < 10000:
        freq += lines[i] 
        print(i)
        if freq in reached:
            i+=1
            found=True
        reached.append(freq)
    return freq
