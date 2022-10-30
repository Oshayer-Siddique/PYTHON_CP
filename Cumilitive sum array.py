n = int(input())  
arr = list(map(int,input().strip().split()))[:n]
m = int(input())
prefixsum = [0 for i in range(n)]
prefixsum[0] = arr[0]
for i in range(1,n):
    prefixsum[i] = prefixsum[i-1] + arr[i]

#print(prefixsum)
for i in range(m):
    u,v = map(int,input().split())
    if u == 0:
        ans = prefixsum[v]
    else:
        ans = prefixsum[v] - prefixsum[u-1]

    print(ans)