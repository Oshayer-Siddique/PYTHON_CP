t = int(input())
while t > 0:
    import math
    n,k = map(int,input().split())
    arr = []
    for i in range(k+1,n+1,+1):
        arr.append(i)
    x = math.ceil(k/2)
    for i in range(x,k,+1):
        arr.append(i)
    print(len(arr))
    print(*arr,sep=" ")
    t = t-1