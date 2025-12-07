#Task: https://adventofcode.com/2025/day/7
f = open('y2025/data/day07.txt', 'r')
lines = f.readlines()
f.close()
from collections import Counter
lines = [s.strip() for s in lines]


def part1():
    count_split = 0
    beam_heads=[]

    for line in lines:
        splitters_in_row = []
        for col, char in enumerate(line):
            if char == "S":
                beam_heads.append(col)
            elif char == "^":
                splitters_in_row.append(col)

        if len(splitters_in_row):
            splitting = list(set(beam_heads) & set(splitters_in_row))

            for split in splitting:
                beam_heads.remove(split)
                if split > 0:
                    beam_heads.append(split-1)
                if split <= len(line)-1:
                    beam_heads.append(split+1)
                count_split += 1
            beam_heads = list(set(beam_heads))     
    return count_split
    # 1711

def part2():
    beam_heads = {} 
    
    for line in lines:
        splitters_in_row = []
        for col, char in enumerate(line):
            if char == "S":
                beam_heads[col] = beam_heads.get(col, 0) + 1
            elif char == "^":
                splitters_in_row.append(col)
        
        splitting = list(set(beam_heads.keys()) & set(splitters_in_row))
        if splitting:
            new_branches = {}

            for split in splitting:
                count = beam_heads.pop(split)
                if split > 0:
                    new_branches[split-1] = new_branches.get(split-1, 0) + count
                if split < len(line)-1:
                    new_branches[split+1] = new_branches.get(split+1, 0) + count

            for col, count in new_branches.items():
                beam_heads[col] = beam_heads.get(col, 0) + count

    return sum(beam_heads.values())
    # 36706966158365
if __name__ == "__main__":
    print()
    print("P1",part1())
    print("P2",part2())