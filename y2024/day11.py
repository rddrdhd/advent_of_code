#Task: https://adventofcode.com/2024/day/11
from collections import defaultdict

f = open('y2024/data/day11.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]


def blink(line,count):
    stones = [int(x) for x in line.split()]
    i = 0
    while i < count:
        new_stones = []
        for num in stones:
            if num == 0:
                new_stones.append(1)
                #print("0 -> 1")
            elif len(str(num)) % 2 == 0:
                string = str(num)
                mid = len(string)//2
                half1, half2 = string[mid:],string[:mid]
                new_stones.append(int(half2))
                new_stones.append(int(half1))
                #print(num,"->",half1,half2)
            else:
                new_stones.append(num*2024)
                #print(num,"->",num*2024)
        stones = new_stones
        i+=1
    return stones


def split_stone(stone):
    mid = len(stone) // 2
    left = stone[:mid]
    right = stone[mid:]
    right = str(int(right)) if right != "0" else "0"
    return left, right


def count_stones(input_str, steps):
    stones = input_str.split()
    stone_count = defaultdict(int) # ALL HAIL OUR LORD DEFAULTDICT

    for stone in stones:
        stone_count[stone] += 1

    for _ in range(steps):
        new_stone_count = defaultdict(int)

        for stone, count in stone_count.items():
            if stone == "0":
                new_stone_count["1"] += count
            elif len(stone) % 2 == 0: 
                left, right = split_stone(stone)
                new_stone_count[left] += count
                new_stone_count[right] += count
            else: 
                new_stone = str(int(stone) * 2024)
                new_stone_count[new_stone] += count
        stone_count = new_stone_count

    total_stones = sum(stone_count.values())
    return total_stones


def part1():
    return len(blink(lines[0], 25))


def part2():
    #stones = blink(lines[0], 75) hahaha just kidding... but yes, I tried...
    result = count_stones(lines[0], 75)
    return result


if __name__ == "__main__":
    print()
    print("P1",part1()) # 229043
    print("P2",part2()) # 272 673 043 446 478 