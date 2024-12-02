#Task: https://adventofcode.com/2024/day/1
f = open('y2024/data/day01.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]

def get_columns(lines):
    aa, bb = [], []
    for l in lines:
        a, b = l.split()
        aa.append(int(a))
        bb.append(int(b))
    return aa, bb

def part1():
    sum = 0
    aa, bb = get_columns(lines)
    aa.sort()
    bb.sort()
    for i in range(len(aa)):
        sum += abs(aa[i]-bb[i])
    return sum

def part2():
    sum = 0
    aa, bb = get_columns(lines)
    for a in aa:
        sum += a*bb.count(a)
    return sum

if __name__ == "__main__":
    print()
    print("P1",part1())
    print("P2",part2())