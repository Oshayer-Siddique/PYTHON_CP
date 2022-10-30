t = int(input())
while t > 0:
    a,b = map(int,input().split())

    ans = min(a,b,(a+b)//3)
    print(ans)
    t = t-1

