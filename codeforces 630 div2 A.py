t = int(input())
while t > 0:
    a,b,c,d = map(int,input().split())
    x,y,x1,y1,x2,y2 = map(int,input().split())
    x = x + (b - a)
    y = y + (d - c)
    if abs(a + b) > 0 and x1 == x2:
        print("NO")
    elif abs(c + d) > 0 and y1 == y2:
        print("NO")
    elif x1 <= x <= x2 and y1 <= y <= y2:
        print("Yes")
    else:
        print("NO")
    #print(x,y)
   
    t = t-1