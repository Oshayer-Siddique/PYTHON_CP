n= int(input())
arr = list(map(int,input().strip().split()))[:n]

dp = [0 for i in range(n)]

dp[0] = 1
for i in range(1,n,1):
    if (arr[i] % 2 == 0 and arr[i-1] % 2 == 0) or ( arr[i] % 2 == 1 and arr[i-1] % 2 == 1):
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = 1

ans = max(dp)
print(ans)