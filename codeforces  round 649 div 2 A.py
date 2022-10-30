t = int(input())
while t > 0:
 
    n,x = map(int,input().split())
    arr = list(map(int,input().strip().split()))[:n]
    arr1 = []
    arr1.extend(arr)
    arr1.reverse()
 
    total_divisible = 0
    s =  sum(arr)
    total = sum(arr1)
    for i in range(n):
        if arr[i] % x == 0:
            total_divisible += 1
    if total_divisible == n:
        print(-1)
    elif sum(arr) % x != 0:
        print(n)
    else:
        for i in range(n):
            s = s - arr[i]
            if s % x != 0:
                ans = i+1
                break
        res = n-ans
 
 
 
        for j in range(n):
            total = total - arr1[j]
            if total % x != 0:
                ans1 = j+1
                break
        res1 = n - ans1
        last = max(res,res1)
        print(last)
 
    t = t-1

