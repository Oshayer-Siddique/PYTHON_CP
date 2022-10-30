t = int(input())
while t > 0:
    n = int(input())
    arr = [None]*n
    for i in range(n):
        arr[i] = list(input())
    stor = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '*':
                stor.append(i)
                stor.append(j)

    x1 = stor[0]
    y1 = stor[1]
    x2 = stor[2]
    y2 = stor[3]

#print(stor)
    if y1 == y2:
        for i in range(n):
            for j in range(n):
                arr[x1][y1-1] = '*'
                arr[x2][y2-1] = '*'
                print(arr[i][j],end="")
            print()
    elif x1 == x2:
        for i in range(n):
            for j in range(n):
                arr[x1-1][y1] = '*'
                arr[x2-1][y2] = '*'
                print(arr[i][j],end="")
            print()
    else:
        for i in range(n):
            for j in range(n):
                if arr[x1][y2] == '.':
                    arr[x1][y2] = '*'
                elif arr[x2][y1] == '.':
                    arr[x2][y1] = '*'
                print(arr[i][j],end="")
            print()
    t = t-1