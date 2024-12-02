#Task: https://adventofcode.com/2024/day/2
f = open('y2024/data/day02.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]



def is_seq_safe(seq):
    s1, s2 = sorted(seq), sorted(seq, reverse=True)
    if seq != s1 and seq != s2:  # Check if sorted
        return False

    # Check differences
    for i in range(1, len(seq)):
        diff = abs(seq[i] - seq[i - 1])
        if not 1 <= diff <= 3:
            return False

    return True


def is_subseq_safe(seq):
    new_lists = [seq[:i] + seq[i+1:] for i in range(len(seq))]
    for subseq in new_lists:
        if is_seq_safe(subseq):
            return 1
    return 0


def part1():
    sum = 0
    for line in lines:
        seq = [int(x) for x in line.split()]
        if is_seq_safe(seq):
            sum += 1
    return sum


def part2():
    sum = 0
    for line in lines:
        seq = [int(x) for x in line.split()]
        if is_seq_safe(seq):
            sum += 1
        else:
            sum += is_subseq_safe(seq)
    return sum

if __name__ == "__main__":
    print()
    print("P1",part1())
    print("P2",part2())