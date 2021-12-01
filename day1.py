# Using readlines()
file1 = open('day1_data.txt', 'r')
Lines = file1.readlines()
 
count = 0
last_line = ""

for line in Lines:
    current_line = line.strip()
    if last_line != "":
        if int(last_line) < int(current_line):
            count+=1
            #print("{} < {} (Increased)".format(last_line, current_line))
        else:
            print("{} >= {} (Decreased)".format(last_line, current_line))
    else:
        print("no last line")
    last_line = current_line

print(count) # 1715