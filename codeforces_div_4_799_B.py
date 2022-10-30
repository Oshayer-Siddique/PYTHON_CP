t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    arr.sort()
    
    
    if arr[0] == arr[-1] and n % 2 ==0:
        count = 0
    else:
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                arr[i] = 0
                arr[i+1] = 0
        count = 0   
        for j in range(len(arr)):
            if arr[j] != 0:
                count += 1


    print(arr)
    print(count)
    t = t-1


    