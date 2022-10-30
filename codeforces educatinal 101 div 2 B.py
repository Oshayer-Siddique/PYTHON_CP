t = int(input())
while t > 0:
    n =  int(input())
    r = list(map(int,input().strip().split()))[:n]
    m = int(input())
    b = list(map(int,input().strip().split()))[:m]

    sum1 = 0
    mx1 = 0
    for i in range(n):
        sum1 = sum1 + r[i]
        mx1 = max(sum1,mx1)

    #print(mx1)

    sum2 = 0
    mx2 = 0
    for j in range(m):
        sum2 = sum2 + b[j]
        mx2 = max(sum2,mx2)

    ans = mx1+mx2
    print(ans)
    t = t-1
