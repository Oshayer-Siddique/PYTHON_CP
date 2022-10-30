import math
t = int(input())
while t > 0:
    x,y = map(int,input().split())
    ans = 0
    if y > x :
        if y % 2 != 0:
            ans = (y * y) - x  + 1
        else:
            ans = (y-1)*(y-1) + x

    else:
        if x % 2 != 0:
            ans = (x-1)*(x-1) + y
        else:
            ans = x * x - y + 1


    print(ans)
    t = t-1












