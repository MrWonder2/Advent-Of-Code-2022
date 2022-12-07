f = open("input.txt")

s = f.read()
for i in range(len(s)):
    x = s[i:i+4]
    if x.count(s[i]) == 1 and x.count(s[i+1]) == 1 and x.count(s[i+2]) == 1 and x.count(s[i+3]) == 1:
        print(i+4)
        break
