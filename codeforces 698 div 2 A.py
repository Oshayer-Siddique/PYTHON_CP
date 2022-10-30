t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    stor = []
    cnt = 0
    num = arr[0]
    for i in arr:
        cur_freq = arr.count(i)
        stor.append(cur_freq)

    ans = max(stor)
    print(ans)
    t = t-1


