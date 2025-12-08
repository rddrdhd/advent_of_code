#Task: https://adventofcode.com/2025/day/8
import math
f = open('y2025/data/day08.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]

def euclidian_distance(p1, p2):
    #print(p1, p2)
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dz = p2[2] - p1[2]
    return math.sqrt(dx*dx + dy*dy + dz*dz)

def get_sorted_pairs(boxes):
    pairs = []
    for x in range(len(boxes)):
        for y in range(x + 1, len(boxes)):
            d = euclidian_distance(boxes[x], boxes[y])
            pairs.append((d, x, y))
    
    pairs.sort()
    return pairs

def part1():

    boxes = [[int(x) for x in l.split(",")] for l in lines]
    pairs = get_sorted_pairs(boxes)
    groups = list(range(len(boxes)))

    if len(boxes) >= 1000:
        iterations = 1000
    else:
        iterations = 10

    for i in range(iterations):
        _, a, b = pairs[i]
        g1, g2 = groups[a], groups[b]
        if g1 != g2:
            for j in range(len(groups)):
                if groups[j] == g1:
                    groups[j] = g2
                    
    counts = {}
    for g in groups:
        counts[g] = counts.get(g, 0) + 1
        
    sizes = sorted(counts.values(), reverse=True)
    return sizes[0] * sizes[1] * sizes[2]
    # 175500

def part2():
    boxes = [[int(x) for x in l.split(",")] for l in lines]
    pairs = get_sorted_pairs(boxes)
    groups = list(range(len(boxes)))

    count_groups = len(boxes) 

    for _, b1, b2 in pairs:
        id1, id2 = groups[b1], groups[b2]
        if id1 != id2:
            for i in range(len(groups)):
                if groups[i] == id1:
                    groups[i] = id2
            count_groups -= 1 # merge
            
            if count_groups == 1: # one big circuit
                x1 = boxes[b1][0]
                x2 = boxes[b2][0]
                return x1 * x2
                # 6934702555

    return -1

if __name__ == "__main__":
    print()
    print("P1",part1())
    print("P2",part2())