f1 = open("input.txt")
count = 0
s = f1.readlines()
for line in s:
    x = line.replace("-", " ").replace(",", " ").split()
    if int(x[0]) <= int(x[2]) and int(x[1]) >= int(x[3]):
        count = count + 1
    elif int(x[2]) <= int(x[0]) and int(x[3]) >= int(x[1]):
        count = count + 1
print(count)
