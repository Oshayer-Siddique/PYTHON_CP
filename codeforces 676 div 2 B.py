
n = int(input())
arr = list(map(int,input().strip().split()))[:n]
m = max(arr)
for j in range(len(arr)-1):
    if arr[j] == arr[j+1]:
        ans = -1
    elif m == arr[-1]:
        ans = len(arr)
    else:
        for i in range(len(arr)-1):
            if arr[i] == m:
                if arr[i] > arr[i+1]:
                    ans = i+1
                elif arr[i] > arr[i-1]:
                    ans = i+1

print(ans)

    
    
