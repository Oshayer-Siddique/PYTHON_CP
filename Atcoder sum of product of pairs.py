# TLE Sucks it

'''n = int(input())
arr = list(map(int,input().strip().split()))[:n]
sum = 0
for i in range(0,n-1,+1):
    for j in range(i+1,n,+1):
        sum = sum + arr[i] * arr[j]


print(sum%(10**9 + 7))  '''

n = int(input())  
arr = list(map(int,input().strip().split()))[:n]    
suf_sm = 0
ans = 0

for i in range(n-1,-1,-1):
    ans = ans + (arr[i] * suf_sm)
    suf_sm += arr[i]
    
print(ans % (10**9 + 7))