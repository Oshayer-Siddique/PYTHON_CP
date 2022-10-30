n,k = map(int,input().split())
arr = list(map(int,input().strip().split()))[:n]


for i in range(n):
    sum = 0
    for j in range(i,n,+1):
        sum += arr[j]

        if sum == k:
            print(arr[i:j+1])
    

