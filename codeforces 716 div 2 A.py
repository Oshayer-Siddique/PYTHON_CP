
import math
t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    flag = 0
    for i in range(n):
        a = math.sqrt(arr[i])
        if math.floor(a) != a:
            flag = 1
            break

    if flag == 1:
        print("YES")
    else:
        print("NO")
    t = t-1