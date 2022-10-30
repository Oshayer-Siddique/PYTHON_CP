t = int(input())
while t > 0:
    n,k = map(int,input().split())
    a,b,c = 0,0,0
    if n % 2 == 1:
        a = n//2
        b = n//2
        c = 1
    elif n % 2 == 0 and n % 4 != 0:
        a = (n - 2)//2
        b = (n-2)//2
        c = 2
    elif  n % 4 == 0:
        a = n// 4
        b = n // 4
        c = n// 2


    print(a,b,c)
    t = t-1