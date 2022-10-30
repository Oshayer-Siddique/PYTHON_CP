t = int(input())
while t > 0:
    r,b,d = map(int,input().split())
    packs = min(r,b)
    if (d+1)*packs < max(r,b):
        print("NO")
    else:
        print("YES")
    t = t-1