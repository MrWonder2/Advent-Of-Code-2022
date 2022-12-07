f1 = open("input.txt")
sum = 0
def priority(x):
    if x.islower():
        return ord(x)-96
    elif x.isupper():
        return ord(x)-38


for line in f1.readlines():
    x = int((len(line))/2)
    y = len(line) 
    new_list_1 = str(line[0:x])
    new_list_2 = str(line[x:y])
    for i in new_list_1:
        if i in new_list_2:
            sum = sum + priority(i)
            break


print(sum)