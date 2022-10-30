t =int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]

    s = sum(arr)
    per_size1 = s//n
#per_size2 = (s//n)+1
#print(per_size1)

    arr1 = [per_size1]*n
#print(arr1)
    extra = s - per_size1*n
    #print(extra)

    for i in range(extra):
        arr1[i] += 1
    arr1.sort()
#print(arr1)
    ans = 0
    for i in range(n):
        for j in range(i+1,n,+1):
            ans += abs(arr1[i] - arr1[j])

    print(ans)
    t = t-1