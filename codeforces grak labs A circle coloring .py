t = int(input())
while(t>0):
    n = int(input())
    a = list(map(int,input().strip().split()))[:n]
    b = list(map(int,input().strip().split()))[:n]
    c = list(map(int,input().strip().split()))[:n]
    p = []

    p.append(a[0])
    for i in range(0,len(a)-1):
        if a[i] == a[i+1]:
            continue
        p.append(a[i+1])

    p.append(b[0])
    for j in range(0,len(b)-1):

        if b[j] == b[j+1]:
            continue
        else:
            p.append(b[j+1])
    p.append(c[0])
    for k in range(0,len(c)-1):
        if c[k] == c[k+1]:
            continue
        else:
            p.append(c[k+1])



    print(p[:n])
    t = t-1
