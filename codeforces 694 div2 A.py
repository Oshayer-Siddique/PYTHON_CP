import math
t = int(input())
while t >0:


    n,x = map(int,input().split())
    arr = list(map(int,input().strip().split()))[:n]
    max = 0
    for i in range(len(arr)):
        max = max + math.ceil(arr[i]/x)

    min = math.ceil(sum(arr)/x)
    print(min,max)
    t = t-1
