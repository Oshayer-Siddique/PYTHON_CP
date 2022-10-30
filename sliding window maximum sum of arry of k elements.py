n ,k = map(int,input().split())
arr = list(map(int,input().strip().split()))[:n]

max_sum = -1000000000000000000000000000000000000000000000000000
for i in range(n-k+1):
    current_sum = 0
    for j in range(k):
        current_sum += arr[i+j]
    max_sum = max(current_sum,max_sum)
print(max_sum)