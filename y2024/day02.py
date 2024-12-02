#Task: https://adventofcode.com/2024/day/2
f = open('y2024/data/day02.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]


def part1():
    sum = 0
    for line in lines:
        passing = True
        nums = [int(x) for x in line.split()]
        s1, s2 = sorted(nums,reverse=False), sorted(nums,reverse=True)
        if s1==nums or s2==nums:
            for i in range(1, len(nums)):
                diff = abs(nums[i-1]-nums[i])
                if not 1<=diff<=3:
                    passing = False
        else:
            passing = False
            
        if passing:
            sum+=1
    return sum

def is_sequence_tolerable(nums):
    s1, s2 = sorted(nums), sorted(nums, reverse=True)
    if nums != s1 and nums != s2:  # Check if sorted
        return False

    # Check differences
    for i in range(1, len(nums)):
        diff = abs(nums[i] - nums[i - 1])
        if not 1 <= diff <= 3:
            return False

    return True


def is_tolerable_pass(nums):
    new_lists = [nums[:i] + nums[i+1:] for i in range(len(nums))]
    for candidate in new_lists:
        if is_sequence_tolerable(candidate):
            return 1
    return 0


def part2():
    total = 0
    for line in lines:
        nums = [int(x) for x in line.split()]
        if is_sequence_tolerable(nums):
            total += 1
        else:
            total += is_tolerable_pass(nums)
    return total

if __name__ == "__main__":
    print()
    print("P1",part1())
    print("P2",part2())