f = open("input.txt")
A = ["W", "D", "G", "B", "H", "R", "V"]
B = ["J", "N", "G", "C", "R", "F"]
C = ["L", "S", "F", "H", "D", "N", "J"]
D = ["J", "D", "S", "V"]
E = ["S", "H", "D", "R", "Q", "W", "N", "V"]
F = ["P", "G", "H", "C", "M"]
G = ["F", "J", "B", "G", "L", "Z", "H", "C"]
H = ["S", "J", "R"]
I = ["L", "G", "S", "R", "B", "N", "V", "M"]


def stacked(num):
    if num == 1:
        return A
    elif num == 2:
        return B
    elif num == 3:
        return C
    elif num == 4:
        return D
    elif num == 5:
        return E
    elif num == 6:
        return F
    elif num == 7:
        return G
    elif num == 8:
        return H
    elif num == 9:
        return I


for line in f.readlines():
    line = line.split()
    temp = []
    for i in range(int(line[1])):
        item = stacked(int(line[3])).pop()
        temp.append(item)
    temp = reversed(temp)
    stacked(int(line[5])).extend(temp)

for i in range(1, 10):
    print(stacked(i).pop(), end="")
