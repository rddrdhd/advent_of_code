#Task: https://adventofcode.com/2023/day/15
f = open('y2023/data/day15.txt', 'r')
lines = f.readlines()
f.close()
lines = [s.strip() for s in lines]

def hash(word):
    hash = 0
    for char in word:
        hash += ord(char)
        hash *= 17
        hash = hash % 256
    return hash

def part1():
    sum = 0
    instructions = lines[0].split(",") # one line input
    for instruction in instructions:
        sum += hash(instruction)
    return sum

def part2():
    sum = 0
    boxes = [[] for _ in range(256)]
    focal_lengths = {}
    instructions = lines[0].split(",") # one line input

    for instruction in instructions:
        if "=" in instruction:
            label, focal_length = instruction.split("=")
            focal_length = int(focal_length)
            index = hash(label)

            if label not in boxes[index]:
                boxes[index].append(label)

            focal_lengths[label] = focal_length
            
        else:
            label = instruction[:-1]
            index = hash(label)

            if label in boxes[index]:
                boxes[index].remove(label)

    for box_index, box in enumerate(boxes):
        for slot_index, label in enumerate(box):
            sum += (box_index+1) * (slot_index+1) * focal_lengths[label]
    return sum