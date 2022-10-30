n = int(input())
arr = list(map(int,input().strip().split()))[:n]
max_len = 0
i = 0
for i in range(n):
    cur_sum = 0
    for j in range(i,n):
        cur_sum += arr[j]
        if cur_sum == 0:
            max_len = max(max_len,j-i+1)

print(max_len)