#Task: https://adventofcode.com/2024/day/9
f = open('y2024/data/day09.txt', 'r')
lines = f.readlines()
f.close()

lines = [s.strip() for s in lines]


def parse_disk_map(disk_map):
    blocks = []
    file_id = 0
    reading_file = True  # disk map begins with a file
    
    for i in range(len(disk_map)):
        length = int(disk_map[i])
        if reading_file:
            for _ in range(length):
                blocks.append(file_id)
            file_id += 1
        else:
            for _ in range(length):
                blocks.append('.')
        reading_file = not reading_file  
    
    return blocks


def compact_disk(blocks):
    for i in range(len(blocks)-1, -1, -1):  # start from the end of the disk
        if blocks[i] != '.':  
            for j in range(len(blocks)):  # find the leftmost free space
                if blocks[j] == '.': # switch
                    blocks[j] = blocks[i]
                    blocks[i] = '.'
                    break 
    return blocks[1:]


def compact_disk2(blocks):
    max_file_id = max(block for block in blocks if block != '.')  # the highest file ID

    for file_id in range(max_file_id, -1, -1):  # start from the last file
        file_indexes = []
        
        for i, block in enumerate(blocks):
            if block == file_id:
                file_indexes.append(i)

        if not file_indexes:
            continue  

        file_length = len(file_indexes)
        file_start_index = min(file_indexes)  # leftmost position of this file

        # find leftmost space for this file
        best_position = None
        for start in range(file_start_index - file_length + 1):
            if start < 0:  
                continue
            block_slice = blocks[start:start + file_length]
            all_space = all(block == '.' for block in block_slice)
            if all_space:
                best_position = start
                break  

        # move file
        if best_position and best_position < file_start_index:
            for idx in file_indexes:
                blocks[idx] = '.'
            for j in range(file_length):
                blocks[best_position + j] = file_id

    return blocks

def calculate_checksum(blocks):
    checksum = 0
    for position, block in enumerate(blocks):
        if block != '.': 
            checksum += position * block
            #print(checksum,"+=",position,"*",block)
    return checksum

def part1():

    disk_map = lines[0]
    blocks = parse_disk_map(disk_map)
    #print(''.join([str(b) for b in blocks]))
    compacted_blocks = compact_disk(blocks)
    #print(''.join([str(b) for b in compacted_blocks]))
    checksum = calculate_checksum(compacted_blocks)
    return checksum


def part2():

    disk_map = lines[0]
    blocks = parse_disk_map(disk_map)
    #print(''.join([str(b) for b in blocks]))
    compacted_blocks = compact_disk2(blocks)
    #print(''.join([str(b) if b else pass for b in compacted_blocks]))
    checksum = calculate_checksum(compacted_blocks)
    return checksum

if __name__ == "__main__":
    print()
    print("P1",part1()) # 6366665108136, 52s
    print("P2",part2()) # 6398065450842, 1m39s