n = int(input())
arr = list(map(int,input().strip().split()))[:n]
hill = 0
valley = 0
for i in range(1,len(arr)-1,+1):
    if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
        hill = hill+1
    elif arr[i] < arr[i+1] and arr[i] < arr[i-1]:
        valley += 1

total = hill+valley
ans = total

minus = 0
for i in range(len(arr)):
    val = arr[i]
    minus = 0
    if i -1 >= 0:
        arr[i] = arr[i-1]
        for j in range(i-1,i+2,+1):
            if(!arr)
    
    