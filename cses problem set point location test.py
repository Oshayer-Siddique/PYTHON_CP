t = int(input())
while t > 0:
    x1,y1,x2,y2,x3,y3 = map(int,input().split())
    det = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

    if det > 0:
        print("LEFT")
    elif det == 0:
        print("TOUCH")
    else:
        print("RIGHT")
    t = t-1