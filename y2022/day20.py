#Task: https://adventofcode.com/2022/day/1
f = open('y2022/data/day20.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]

#WIP: work s on test data

def part1():
    numbers = [int(s for s in lines]
    len_numbers = len(numbers)
    final_numbers = numbers.copy()
    for n in numbers:
        #print(final_numbers)
        i = final_numbers.index(n)
        final_numbers.remove(n)

        new_i = i + n
        if new_i <= 0:
            new_i = len_numbers + (new_i - 1)
        elif new_i >= len_numbers:
            new_i = (new_i % len_numbers) + 1
        #print(n,"->",new_i)
        final_numbers.insert(new_i, n)
    #print(final_numbers)
    k1 = final_numbers[(1000 + final_numbers.index(0)) % len_numbers]
    k2 = final_numbers[(2000 + final_numbers.index(0)) % len_numbers]
    k3 = final_numbers[(3000 + final_numbers.index(0)) % len_numbers]
    print("(",k1, ") + (", k2, ") + (", k3, end=" ) = ")
    return k1 + k2 + k3  # not -4824


def part2():
    return 0
