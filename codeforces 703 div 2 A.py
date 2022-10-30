t = int(input())
while t > 0:

    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    sum = 0
    flag = 0
    for i in range(n):
        
        sum = sum+arr[i]
        need = (i*(i+1))/2
        if sum < need:
            flag = 1
            break
    if flag == 1:
        print("NO")
    else:
        print("YES")
    t = t-1
