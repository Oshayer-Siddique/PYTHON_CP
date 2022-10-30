t = int(input())
while t > 0:
    n = int(input())
    m = 2*n
    arr = list(map(int,input().strip().split()))[:m]
    odd ,even = 0 , 0
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            odd +=1
        else:
            even +=1

    if odd == even:
        print("Yes")
    else:
        print("No")
    t = t-1
