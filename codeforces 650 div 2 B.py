t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    even = 0
    odd = 0
    cnt = 0
    for j in range(n):
        if arr[j] % 2 == 0:
            even += 1
        elif arr[j] % 2 == 1:
            odd +=1
    if abs(even-odd) > 1:
        ans = -1
    else:
        for i in range(n):
            if i % 2 != arr[i] % 2:
                cnt += 1
        if cnt % 2 == 0:
            ans = cnt//2
        else:   
            ans = -1

    print(ans)
    t = t-1 