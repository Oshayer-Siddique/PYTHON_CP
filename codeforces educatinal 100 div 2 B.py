t = int(input())
while t >0:
    n = int(input())
    a = list(map(int,input().strip().split()))[:n]
    b = []
    even = 0
    odd = 0
    for i in range(n):
        if i % 2 == 0:
            even = even+a[i]
    for i in range(n):
        if i % 2 == 1:
            odd = odd+a[i]

    if even > odd:
        for j in range(n):
            if j % 2 == 1:
                b.append(1)
            else:
                b.append(a[j])
    elif odd > even:
        for k in range(n):
            if k % 2 == 0:
                b.append(1)
            else:
                b.append(a[k])
    elif odd == even:
        for m in range(n):
            if m % 2 == 0:
                b.append(1)
            else:
                b.append(a[m])

    print(*b,sep=' ')
    t = t-1
