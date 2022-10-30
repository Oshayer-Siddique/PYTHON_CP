
def ori(xa,ya,xb,yb,xc,yc):
    det = (xa*yb + xb*yc + xc*ya) - (xb*ya + xc*yb + xa*yc)
    if det > 0:
        return 1
    elif det < 0:
        return 2
    else:
        return 0

def on_segment(xa,ya,xb,yb,xc,yc):
    if (min(xa,xb) <= xc <= max(xa,xb)) and (min(ya,yb) <= yc <= max(ya, yb)):
        return 1
    else:
        return 0
t = int(input())
while t > 0:

    x1,y1,x2,y2,x3,y3, x4, y4 = map(int,input().split())

    ori1 = ori(x1,y1,x2,y2,x3,y3)
    ori2 = ori(x1,y1,x2,y2,x4,y4)
    ori3 = ori(x3,y3,x4,y4,x1,y1)
    ori4 = ori(x3,y3,x4,y4,x2,y2)


    if (ori1 != ori2 ) and (ori3 != ori4):
        print("YES")
    elif ori1 == 0 and (on_segment(x1,y1,x2,y2,x3,y3)) == 1:
        print("YES")
    elif ori2 == 0 and(on_segment(x1,y1,x2,y2,x4,y4)) == 1:
        print("YES")
    elif ori3 == 0 and (on_segment(x3,y3,x4,y4,x1,y1)) == 1:
        print("YES")
    elif ori4 == 0 and (on_segment(x3,y3,x4,y4,x2,y2)) == 1:
        print("YES")
    else:
        print("NO")
    t = t-1