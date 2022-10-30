t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int,input().strip().split()))[:n]
    b = list(map(int,input().strip().split()))[:n]
    y = 0
    for k in range(1,n):
        if a[k] < a[k-1]:
            y = 1
            break
    if y == 0:
        print("Yes")
    else:
        flag1 = 0
        flag2 = 0
        for i in range(n):
            if b[i] == 0:
                flag1 = 1
                break
        for j in range(n):
            if b[j] == 1:
                flag2 = 1
                break
        if flag1 == 1 and flag2 == 1:
            print("Yes")
        else:
            print("No")
    t = t-1