
print("Codeforces 675 div 2 B :: Nice Matrix ")
t = int(input())
while(t>0):
    row,col = map(int,input().split())
    def func(a,b,c,d):
        v = []
        v.append(a)
        v.append(b)
        v.append(c)
        v.append(d)
        v.sort()
        return ((v[1]+v[1])//2)

    arr = []
    for k in range(row):
        a = list(map(int,input().split()))[:col]
        arr.append(a)
    fin = 0
    ans = [[0]*col]*row
    for i in range(row):
        for j in range(col):
            u = func(arr[i][j],arr[row-i-1][j],arr[i][col-j-1],arr[row-1-i][col-1-j])
            ans[i][j] = u
            fin = fin + abs(arr[i][j]-ans[i][j])
    print(fin)
    t=t-1
