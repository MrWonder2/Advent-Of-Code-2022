f1 = open("input.txt")
sum = 0
def priority(x):
    if x.islower():
        return ord(x)-96
    elif x.isupper():
        return ord(x)-38

l = f1.readlines()

for ele_num in range(0,len(l),3):
    x = l[ele_num][:-1]
    y = l[ele_num+1][:-1]
    z = l[ele_num+2][:-1]
    for i in x:
        if i in y:
            if i in z:
                sum = sum + priority(i)
                break

print(sum)