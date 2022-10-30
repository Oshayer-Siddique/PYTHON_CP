t = int(input())
while t > 0:
    n ,k = map(int,input().split())
    p = list(map(int,input().strip().split()))[:n]
    ps = [0]*n
    ps[0] = p[0]
    for i in range(1,n,+1):
        ps[i]  = p[i] + ps[i-1]

    inc = 0
    for i in range(n-1,0,-1):
        temp = k*(ps[i-1] +inc)
        if 100*p[i] < temp:
            continue
        else:
            x = (100*p[i] - (ps[i-1] +inc)*k + k-1)//k
            inc += x

    print(inc)
    t = t-1 




   