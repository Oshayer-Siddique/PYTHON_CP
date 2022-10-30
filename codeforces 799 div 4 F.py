

t = int(input())
while t > 0:
    n  = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    flag = 0
    for i in range(0,n - 2,+1):
        l = i+1
        r = n - 1
        while l < r:
            if arr[i] + arr[l] + arr[r]  % 10 == 3:
                flag = 1
                break

            else:
                l += 1
                r -= 1


    if flag == 1:
        print("YES")
    else:
        print("NO")
    t = t-1
    


             
             