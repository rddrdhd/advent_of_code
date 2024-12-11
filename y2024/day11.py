#Task: https://adventofcode.com/2024/day/11
f = open('y2024/data/day11.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]


def blink(nums,count):
    i = 0
    while i < count:
        new_nums = []
        for num in nums:
            if num == 0:
                new_nums.append(1)
                #print("0->1")
            elif len(str(num)) % 2 == 0:
                string = str(num)
                half1, half2 = string[len(string)//2:],string[:len(string)//2]
                new_nums.append(int(half2))
                new_nums.append(int(half1))
                #print(num,"->",half1,half2)
            else:
                new_nums.append(num*2024)
                #print(num,"->",num*2024)
        #print(new_nums)
        nums = new_nums
        i+=1
    return nums


def part1():
    sum = 0
    nums = [int(n) for n in lines[0].split()]
    sum = len(blink(nums, 25))
    return sum


def part2():
    sum = 0
    nums = [int(n) for n in lines[0].split()]
    # nah :D this wont work
    #sum = len(blink(nums, 75))
    return sum


if __name__ == "__main__":
    print()
    print("P1",part1())
    print("P2",part2())