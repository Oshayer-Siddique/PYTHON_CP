t = int(input())
while t > 0:
    n,m = map(int,input().split())
    arr = []
    for i in range(n):
        a = list(map(int,input().split()))[:m]
        arr.append(a)
    r = [0 for i in range(n)]
    c = [0 for i in range(m)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                r[i] += 1
                c[j] += 1
    d = r.count(0)
    e = c.count(0)
    if min(d,e) % 2 == 0:
        print("Vivek")
    else:
        print("Ashish")
    t = t-1

