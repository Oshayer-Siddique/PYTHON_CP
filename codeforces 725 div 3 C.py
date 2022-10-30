t = int(input())
while t > 0:
    n,l,r = map(int,input().split())
    arr = list(map(int,input().strip().split()))[:n]

    cnt = 0
    for i in range(n-1):
        for j in range(i+1,n,+1):
            if arr[j] == arr[j-1]:
                j+=1
            if arr[i] + arr[j] >= l and arr[i] + arr[j] <= r:
                    j += 1
                    cnt+=1
            else:
                i+=1
       

    print(cnt)
    t = t-1



