t = int(input())
while t > 0:
    n,k = map(int,input().split())
    arr = []
    for i in range(k-3):
        arr.append(1)

    a,b,c = 0,0,0
    if (n-k+3) % 2 == 1:
        a = (n-k+3)//2
        b = (n-k+3)//2
        c = 1
    elif (n-k+3) % 2 == 0 and (n-k+3) % 4 != 0:
        a = (n-k+3-2)//2
        b = (n-k+3-2)//2
        c = 2
    elif  (n-k+3) % 4 == 0:
        a = (n-k+3)// 4
        b = (n-k+3) // 4
        c = (n-k+3)// 2

    arr.append(a)
    arr.append(b)
    arr.append(c)

    print(*arr,sep=" ")
    t = t-1