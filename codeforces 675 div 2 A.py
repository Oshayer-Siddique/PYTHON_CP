t = int(input())
while(t>0):
    a,b,c = map(int,input().split())

    if a == b == c:
        res = a
    else:
        res = (a+b+c)-1

    print(res)
    t = t-1
