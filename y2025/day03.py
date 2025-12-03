#Task: https://adventofcode.com/2025/day/3
f = open('y2025/data/day03.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]

def max_battery_chain(joltages, num_of_batteries):
    n = len(joltages)
    matrix = [[0] * (num_of_batteries + 1) for _ in range(n + 1)] # largest chains
    for i in range(1, n + 1):
        digit = joltages[i - 1]
        for j in range(num_of_batteries + 1):
            matrix[i][j] = matrix[i - 1][j] # skip
        for j in range(1, num_of_batteries + 1):
            if i >= j:
                candidate = matrix[i - 1][j - 1] * 10 + digit
                matrix[i][j] = max(matrix[i][j], candidate)
    return matrix[n][num_of_batteries]

def part1():
    sum = 0
    for bank in lines:
        joltages = [int(x) for x in bank]
        max_joltage = 0
        best_pair = None
        
        for i in range(len(joltages)):
            for j in range(i+1, len(joltages)):
                candidate = joltages[i] * 10 + joltages[j]
                if candidate > max_joltage:
                    max_joltage = candidate
                    best_pair = (i, j)
        sum += max_joltage
    return sum # 17524

def part2():
    num_of_batteries = 12
    sum = 0
    for bank in lines:
        joltages = [int(x) for x in bank]
        n, k = len(joltages), num_of_batteries

        max_num = max_battery_chain(joltages, k)
        
        sum += max_num
    
    return sum # 173848577117276

if __name__ == "__main__":
    print()
    print("P1",part1())
    print("P2",part2())