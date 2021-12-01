# Using readlines()
file = open('day1_data.txt', 'r')
Lines = file.readlines()
sliding_window_size = 3
count = 0
last_window = []
current_window = []
iterations = range(0,int(len(Lines)-(sliding_window_size)))
for i in iterations:
    current_window = [int(Lines[i]),int(Lines[i+1]),int(Lines[i+2])]
    if(sum(current_window) > sum(last_window)):
        count+=1
        #debug prints for start and end
        if(i < 5 or i > 1995):
            print(current_window)
            print("{}>{}".format(sum(current_window) , sum(last_window)))
    last_window = current_window
print("count:",count)