import math
t = int(input())
while t > 0:
    a,b = map(int,input().split())
    ans = 0
    if a == b:
        ans = 0
    else:
        ans = math.ceil(abs(a-b)/10)


    print(ans)
    t = t-1