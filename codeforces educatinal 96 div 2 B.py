t = int(input())
while(t>0):
    n,k = map(int,input().split())
    arr = list(map(int,input().strip().split()))
    
    arr.sort()
    arr.reverse()
    mmaxim = max(arr)
    #print(arr)
    #print(mmaxim)
    sum = 0
    for i in range(k+1):
        sum = sum+ arr[i]

    print(sum)
    t  = t-1

