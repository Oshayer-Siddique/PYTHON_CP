import math
t = int(input())
while t > 0:
 
    n = int(input())
    arr = list(map(int, input().strip().split()))[:n]
    summa = sum(arr)
    c1 = math.ceil(summa / (n - 1))
    s = c1 * (n - 1)
    arr.sort()
    if arr[n - 1] > c1:
        s = arr[n - 1] * (n - 1)
    ans = s - summa
    print(ans)
    t = t - 1
