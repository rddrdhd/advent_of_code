#Task: https://adventofcode.com/2024/day/19
f = open('y2024/data/day19.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]


def construct_design(design, towels, memo, part_two=False):
    if design in memo:
        return memo[design]
    
    if design == "":
        return 1 

    total_ways = 0

    for towel in towels:
        if design.startswith(towel):
            remainder = design[len(towel):]
            result = construct_design(remainder, towels, memo, part_two)

            if part_two:
                total_ways += result  
            elif result: 
                memo[design] = 1
                return 1 

    if part_two:
        memo[design] = total_ways
        return total_ways
    else:
        memo[design] = 0
        return 0


def solve(part_two=False):
    total = 0
    towels = lines[0].split(", ")
    designs = lines[2:]

    for design in designs:
            total += construct_design(design, towels, {}, part_two)

    return total


def part1():
    return solve()


def part2():
    return solve(part_two=True)


if __name__ == "__main__":
    print()
    print("P1",part1()) # 306
    print("P2",part2()) # 604622004681855