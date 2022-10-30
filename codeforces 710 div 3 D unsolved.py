n = int(input())
arr = list(map(int,input().strip().split()))[:n]
cnt = 0

for i in range(n-1):
    for j in range(i+1,n):
        
        print(arr[i],arr[j])
        


