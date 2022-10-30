t = int(input())
while t > 0:
    u = input()
    xa,ya = map(int,input().split())
    xb,yb = map(int,input().split())
    xf ,yf = map(int,input().split())
    ans = 0
    dis = abs(xa-xb) + abs(ya-yb)
 
    if (ya == yb == yf) and (min(xa,xb)<xf and max(xa,xb)>xf):
        ans = dis+2
    elif (xa == xb == xf) and (min(ya,yb) <yf and max(ya,yb)>yf):
        ans = dis+2
    else:
        ans = dis
    
    print(ans)
    
    t = t-1