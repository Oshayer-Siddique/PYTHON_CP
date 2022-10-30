
t = int(input())
while(t>0):
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]

    m = max(arr)

    ind = -1
    for i in range(len(arr)):
        
        if (arr[i] != m):
            continue
        if (i > 0 and arr[i-1]!=m):
            ind = ind+1
        if (i<n-1 and arr[i+1]!=m):
            ind = ind+1

    print(ind)
    t = t-1    