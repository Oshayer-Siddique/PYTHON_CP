t = int(input())
while t > 0:
    n,k = map(int,input().split())
    s = str(input())
    a = ""
    b = ""
    if 2 * k >= n:
        print("NO")
    elif k == 0:
        print("YES")
    else: 
        for i in range(k):
            a = a + s[i]
        for i in range(1,k+1):
            b = b + s[-i]
        if a == b:
            print("YES")
        else:
            print("NO")
    t = t-1


