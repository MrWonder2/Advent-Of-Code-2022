f = open("input.txt")

s = f.read()
for i in range(len(s)):
    x = s[i:i+14]
    if x.count(s[i]) == 1 and x.count(s[i+1]) == 1 and x.count(s[i+2]) == 1 and x.count(s[i+3]) == 1 and x.count(s[i+4]) == 1 and x.count(s[i+5]) == 1 and x.count(s[i+6]) == 1 and x.count(s[i+7]) == 1 and x.count(s[i+8]) == 1 and x.count(s[i+9]) == 1 and x.count(s[i+10])== 1 and x.count(s[i+11])== 1 and x.count(s[i+12])== 1 and x.count(s[i+13])== 1 and x.count(s[i+14])== 1:
        print(i+14)
        break
