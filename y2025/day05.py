#Task: https://adventofcode.com/2025/day/5
f = open('y2025/data/day05.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]


def part1():
    sum = 0
    reading_ranges = True
    ranges = []
    ids = []
    for line in lines:
        if reading_ranges:
            if "-" not in line:
                reading_ranges = False
                continue
            x,y = line.split("-")
            ranges.append((int(x),int(y)))
        else:
            ids.append(int(line))
    for i in ids:
        spoiled = True
        for r in ranges:
            if i in range(r[0],r[1]+1):
                spoiled = False
                continue
        if not spoiled:
            sum += 1

    return sum
    # 865

def part2():
    sum = 0
    ranges = []
    for line in lines:
        if "-" in line:
            x,y = line.split("-")
            ranges.append((int(x),int(y)))
        else: break
            
    union_ranges = []
    for begin, end in sorted(ranges):
        if union_ranges and union_ranges[-1][1] >= begin - 1:
            union_ranges[-1][1] = max(union_ranges[-1][1], end)
        else:
            union_ranges.append([begin, end])
            
    for r in union_ranges:
        sum += r[1]-r[0]+1
    return sum
    # 352556672963116

if __name__ == "__main__":
    print()
    print("P1",part1())
    print("P2",part2())