#Task: https://adventofcode.com/2025/day/6
f = open('y2025/data/day06.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.rstrip('\r\n') for s in lines]  


def part1():
    ops = lines[-1].split()
    sums = [0 for _ in range(len(ops))]
    for line in lines[:-1]:
        line_nums = [int(x) for x in line.split()]
        for i, num in enumerate(line_nums):
            if ops[i] == '+':
                sums[i] += num
            else:
                if sums[i] == 0:
                    sums[i] = 1
                sums[i] *= num
    return sum(sums)
    # 3785892992137

def part2():
    max_len = max(len(l) for l in lines)
    padded = [l.ljust(max_len) for l in lines] # rectangle time!
    op_line = padded.pop()
    matrix_2d = padded
    
    total = 0
    curr_nums = []
    curr_op = None
    for col in range(max_len-1, -1, -1):
        column_str = "".join(row[col] for row in matrix_2d).strip()
        if not column_str: # digits
            if curr_nums:
                if curr_op == '+':
                    total += sum(curr_nums)
                elif curr_op == '*':
                    p = 1
                    for n in curr_nums: p *= n
                    total += p
                curr_nums = []
                curr_op = None
        else: # empty col
            curr_nums.append(int(column_str))
            if op_line[col] in "+*":
                curr_op = op_line[col]
    if curr_nums:
        if curr_op == '+':
            total += sum(curr_nums)
        elif curr_op == '*':
            p = 1
            for n in curr_nums: p *= n
            total += p
            
    return total
    # 7669802156452
        
if __name__ == "__main__":
    print()
    print("P1",part1())
    print("P2",part2())