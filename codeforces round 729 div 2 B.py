t = int(input())
while t > 0:
    n,a,b = map(int,input().split())
    flag = 0
    s = 1
    while s <= n:
        if (n - s) % b == 0:
            flag = 1
            break
        s = s*a

    if flag == 1:
        print("Yes")
    else:
        print("No")
    t = t-1