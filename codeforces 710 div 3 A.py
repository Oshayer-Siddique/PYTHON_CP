import math
t = int(input())
while t > 0:

    n,m,x = map(int,input().split())
    col = x % n
    row  = math.ceil(x/n)
    if col == 0:
        col = n
    ans = m*(col-1) + row
    

    print(ans)
    t = t-1