file = open('day1_data.txt', 'r')
Lines = file.readlines()
file.close()
sliding_window_size = 3
count = 0
last_window = []
current_window = []

for i in range(0,int(len(Lines)-(sliding_window_size))):
    current_window = [int(Lines[i]),int(Lines[i+1]),int(Lines[i+2])]

    if(sum(current_window) > sum(last_window)):
        count+=1

    last_window = current_window
    
print("count:",count)