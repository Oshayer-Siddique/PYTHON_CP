t = int(input())
while t > 0:
    n = int(input())    
    arr = list(map(int,input().strip().split()))[:n]
    cnt = 0
    for i in range(1,n):
        if arr[i] > arr[0]:
            cnt+=1

    print(cnt)
    t = t-1
