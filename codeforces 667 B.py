t = int(input())
while t > 0:

    a,b,x,y,n = map(int,input().split())
    ans = 0
    def check(a,b,x,y,n):
        d1 = a - x
        d2 = b - y
        c1 = min(d1,n)
        a  -= c1
        n -= c1
        c2 = min(d2,n)
        b -= c2
        n -= c2
        ans =a * b
        return ans

    u = check(a,b,x,y,n)
    v = check(b,a,y,x,n)

    last = min(u,v)

    print(last)
    t = t-1

