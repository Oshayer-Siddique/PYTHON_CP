import math
t  = int(input())


 
while t > 0:
 
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    list1 = []
    for i in range(n):
        if arr[i] % 2 == 0:
            list1.append(arr[i])
 
 
    for i in range(n):
        if arr[i] % 2 == 1:
            list1.append(arr[i])
 
    cnt = 0
    for i in range(n-1):
        for j in range(i+1,n,+1):
            if (math.gcd(list1[i],2*list1[j])) > 1:
                cnt+=1
 
    print(cnt)
    t = t-1
