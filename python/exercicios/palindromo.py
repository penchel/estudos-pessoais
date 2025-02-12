string = "abca"
pivot = len(string)
res = True
for x in range(pivot):
    if(string[x] != string[pivot-1-x]):
        res = False
        break
print(res)