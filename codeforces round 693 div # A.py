t = int(input())
while t > 0:
    w,h,n = map(int,input().split())
    d = 1
   
    while  w % 2 == 0:
        w = w//2
        d = d*2
    while h % 2 == 0:
        h =   h//2
        d = d*2
    if d >= n:
        print("YES")
    else:
        print("NO")
    t =t-1