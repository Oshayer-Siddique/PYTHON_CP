u = int(input())
while u > 0:
    n,x,t = map(int,input().split())
    start = []
    for i in range(n):
        start.append(i*x)

#print(start)

    end = []
    for i in range(n):
        end.append(start[i]+t)

#print(end)

    stor = []
    for k in range(n-1):
        a = end[k]

        cnt = 0
        for j in range(k+1,n,+1):
            if a >= start[j] and a <= end[j]:
                cnt+=1
    

        stor.append(cnt)

    print(sum(stor))
    u = u-1