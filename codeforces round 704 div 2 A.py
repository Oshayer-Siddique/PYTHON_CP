import math
t = int(input())
while t > 0:

    p,a,b,c = map(int,input().split())  
    x = math.ceil(p//a)
    y = math.ceil(p//b)
    z = math.ceil(p//c)
    ans = min(x*a,y*b,z*c) - p
    print(ans)
    t = t-1