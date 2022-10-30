n ,s = map(int,input().split())
coins = list(map(int,input().strip().split()))[:n]

arr = [[0 for i in range(s+1)] for i in range(n)]

for i in range(n):
    arr[i][0] = 1
    
for i in range(0,n,+1):
    for j in range(0,s+1,+1):
        if coins[i] > j:
            arr[i][j] = arr[i-1][j]
        else:
            arr[i][j] = arr[i-1][j] + arr[i][j - coins[i]]

ans = arr[n-1][s]    
print(ans)



