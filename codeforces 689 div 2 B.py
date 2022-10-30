t = int(input())
while t > 0:
    n,m = map(int,input().split())
    arr = []
    for k in range(n):
        a = list(map(str,input().split()))[:m]
        arr.append(a)



    for i in range(n):
        for j in range(m):
            if arr[i][j] == '*':
                arr[i][j] = 1
            elif arr[i][j] == '.':
                arr[i][j] = 0


    for i in range(n-2,-1,-1):
        for j in range(m-2,0,-1):
            if arr[i][j] == 1:
                arr[i][j] = 1+(min(arr[i+1][j-1],arr[i+1][j],arr[i+1][j+1]))
    ans = 0
    for i in range(n):
        for j in range(m):
            ans = ans+arr[i][j]

    print(ans)
    t = t-1

    