f1 = open("input.txt")

sum_calories = []
sum = 0
for line in f1.readlines():
    if line == "\n":
        sum_calories.append(sum)
        sum = 0
    else:
        sum = sum + int(line)

# print(sum_calories.index(max(sum_calories)))
sum_calories.sort()

print(sum_calories[0:3])
print(sum_calories[-1:-4:-1])

print(sum_calories[-1]+sum_calories[-2]+sum_calories[-3])