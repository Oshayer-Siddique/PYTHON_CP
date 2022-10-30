n = int(input())
arr = list(map(int,input().strip().split()))[:n]
lis = [1 for i in range(n)]
for i in range(1,n,+1):
    for j in range(0,i,+1):
        if arr[i] > arr[j]:
            if lis[i] <= lis[j]:
                lis[i] = lis[j] + 1
    
ans = max(lis)
print(ans)




def longestSub(arr,n):
    lis = [1 for i in range(n)]
    for i in range(1,n,+1):
        for j in range(0,i,+1):
            if arr[i] > arr[j]:
                if lis[i] <= lis[j]:
                    lis[i] = lis[j] + 1
    return max(lis)

n = int(input())
arr = list(map(int,input().strip().split()))[:n]
print(longestSub(arr,n))