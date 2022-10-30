t = int(input())
while t > 0:
    s = str(input())
    n = len(s)
    l = s.count('L')
    r = s.count('R')
    u = s.count('U')
    d = s.count('D')
    min1 = min(l,r)
    min2 = min(u,d)
    arr = []
    if ( l+d == n or r+d == n or l+u == n or r+u == n):
        print(0)
        print()
    else:
        for i in range(min1):
            arr.append('R')
        for i in range(min2):
            arr.append('U')
        for i in range(min1):
            arr.append('L')
        for i in range(min2):
            arr.append('D')
        if u == 0 or d == 0:
            print(2)
            print("LR")
        elif l == 0 or r == 0:
            print(2)
            print("UD")
        else:
    
            print(len(arr))
            print(*arr,sep="")
    t = t-1

