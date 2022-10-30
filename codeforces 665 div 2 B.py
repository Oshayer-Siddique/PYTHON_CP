t = int(input())
while t > 0:
    x0 , x1 , x2 = map(int,input().split())
    y0 , y1 , y2 = map(int,input().split())
    total = 0
    a = min(x0,y2)
    y2 -= a
    b = min(x1,y0)
    x1 -= b

    m = min(x2,y1)
    total += 2*m
    total -= 2*min(x1,y2)
    print(total)
    t = t-1