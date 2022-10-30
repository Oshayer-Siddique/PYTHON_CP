'''n = int(input())
arr = list(map(int,input().strip().split()))[:n]
u = len(arr)
for i in range(2):
    for j in range(i+1,3,+1):
        if arr[i] != arr[j]:
            arr.remove(arr[i])
            
            
            

print(arr)'''