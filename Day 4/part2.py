f1 = open("input.txt")
s = f1.readlines()
new_count = 0
for line in s:
    x = line.replace("-", " ").replace(",", " ").split()
    x[0] = int(x[0])
    x[1] = int(x[1])
    x[2] = int(x[2])
    x[3] = int(x[3])
    if x[0] < x[2] and x[1] < x[3] and (max(x[0], x[1]) < min(x[2], x[3])):
        new_count = new_count + 1
    elif x[0] > x[2] and x[1] > x[3] and (min(x[0], x[1]) > max(x[2], x[3])):
        new_count = new_count + 1


print(1000-new_count)
