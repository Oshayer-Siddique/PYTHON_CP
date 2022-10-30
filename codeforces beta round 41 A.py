n , v = map(int,input().split())
arr = list(map(int,input().strip().split()))[:n]
brr = list(map(int,input().strip().split()))[:n]
mn = 10000000000000
for i in range(n):
    mn = min(mn,brr[i]/arr[i])
sum = 0
for i in range(n):
    sum = sum + arr[i] * mn

if sum > v:
    print(v)
else:
    print(sum)
    
    