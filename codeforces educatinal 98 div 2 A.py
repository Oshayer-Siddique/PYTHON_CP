t = int(input())
while(t>0):
    x,y = map(int,input().split())
    if y<x:
        ans = (y*2)+((x-y)*2)-1
    elif x<y:
        ans = (x*2)+((y-x)*2)-1
    elif x == y:
        ans = x+y

    print(ans)
    t = t-1
