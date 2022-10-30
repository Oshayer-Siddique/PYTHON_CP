from collections import defaultdict


n = int(input())
arr  = list(map(int,input().strip().split()))[:n]
j = 0
index = defaultdict(lambda : 0)
ans , j = 0, 0 
for i in range(n):
    j = max(index[arr[i]],j)
    ans = max(ans,i - j + 1)
    index[arr[i]] = i+1
    i += 1

print(ans)

