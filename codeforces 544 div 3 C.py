n = int(input())
arr = list(map(int,input().strip().split()))[:n]
arr.sort()
j = 0
ans = 0
for i in range(n):
    while j<n and (arr[j] - arr[i] <=  5): 
        j += 1 
        ans = max(ans , j-i)        
        

print(ans)

