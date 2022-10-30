t = int(input())
while t > 0:
    n,u,r,d,l = map(int,input().split())
    u1 ,r1,d1,l1 = u,r,d,l
    if u == n:
        r1-=1
        l1-=1
    if r == n:
        u1 -= 1
        d1 -= 1
    if d == n:
        r1 -= 1
        l1 -= 1
    if l == n:
        d1 -= 1
        u1 -= 1
    if u == n-1:
        if l1 > r1:
            l1 -= 1
        else:
            r1 -= 1
    if r == n-1:
        if u1 > d1:
            u1 -= 1
        else:
            d1 -= 1
    if d == n-1:
        if l1 > r1:
            l1-=1
        else:
            r1 -= 1
    if l == n-1:
        if u1 > d1:
            u1 -= 1
        else:
            d1 -= 1
    if (u1 < 0) or (r1 < 0) or (d1 < 0)  or (l1 < 0):
        print("NO")
    else:
        print("YES")
    t = t-1
