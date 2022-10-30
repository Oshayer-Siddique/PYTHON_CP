arr = []
for i in range(5):
    a = list(map(int,input().split()))[:5]
    arr.append(a)

#print(arr)

for i in range(5):
    for j in range(5):
        if arr[i][j] == 1:
            curx = (i+1)
            cury = (j+1)
path = abs(curx-3)+abs(cury-3)
print(path)