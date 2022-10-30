t = int(input())
while t > 0:
    x,y,k = map(int,input().split())
    ans = (x-1) + x * (y-1)
    if ans == k:
        print("YES")
    else:
        print("NO")
    t = t-1