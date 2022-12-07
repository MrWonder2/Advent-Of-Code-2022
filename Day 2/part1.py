f1 = open("input.txt")
sum = 0
for line in f1.readlines():
    line = line.split()

    if line[0] == "A": #ROCK
        if line[1] == "X": #R
            sum = sum + 1 + 3 
        if line[1] == "Y": #P
            sum = sum + 2 + 6 
        if line[1] == "Z": #S
            sum = sum + 3 + 0


    if line[0] == "B": #P
        if line[1] == "X": #R
            sum = sum + 1 + 0 
        if line[1] == "Y": #P
            sum = sum + 2 + 3 
        if line[1] == "Z": #S
            sum = sum + 3 + 6 


    if line[0] == "C": #S
        if line[1] == "X":
            sum = sum + 1 + 6 
        if line[1] == "Y":
            sum = sum + 2 + 0 
        if line[1] == "Z":
            sum = sum + 3 + 3 
print(sum)