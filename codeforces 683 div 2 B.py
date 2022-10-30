t = int(input())
while(t>0):
    n,m = map(int,input().split())
    arr = []
    for k in range(n):
        a = list(map(int,input().split()))[:m]
        arr.append(a)
    c = 0
    sum = 0
    mi = 1000
    for i in range(n):
        for j in range(m):
            if arr[i][j] < 0:
                c = c+1
            mi = min(mi,abs(arr[i][j]))
            sum = sum + abs(arr[i][j])

    if c % 2 == 0:
        print(sum)
    else:
        print(sum-2*mi)
    t = t-1



        
    
