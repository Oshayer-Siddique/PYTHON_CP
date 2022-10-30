t = int(input())
while t > 0:
    n = int(input())
    arr = [0] + list(map(int,input().strip().split()))[:n]
    flag = 0
    for i in range(1,n-1):
        for j in range(2,n,+1):
            for k in range(3,n+1,+1):
                if i < j < k:
                    if arr[j] > arr[i] and arr[j] > arr[k]:
                        flag = 1
                        break

    if flag == 1:
        print("YES")
        print(i,j,k)
    else:
        print("NO")
    t = t-1
    