t = int(input())
while t > 0:
    s = str(input())
    arr = list(s)
    stor = []

    for i in range(len(arr)):
        if arr[i] == '1':
            stor.append(i)
    cnt = 0
#print(stor)
    for i in range(len(stor)-1):
        if stor[i+1] - stor[i] > 1:
            cnt+= stor[i+1] - stor[i] - 1

    print(cnt)
    t = t-1

