n = int(input())
arr = list(map(int,input().strip().split()))[:n]
stor = []
for i in range(1,n,+1):
    if arr[i] < arr[i-1]:
        stor.append(arr[i-1] - arr[i])

print(sum(stor))