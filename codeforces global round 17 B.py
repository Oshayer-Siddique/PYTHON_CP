def chkpalin(arr,x):
        i = 0
        j = n - 1
        while i < j:
            if  arr[i] == x:
                i = i+1
            elif arr[j] == x:
                j = j - 1
            elif arr[i] != arr[j]:
                return False
            else:
                i = i+1
                j = j-1
        return True
t = int(input())
while t > 0:



    n = int(input())
    arr = list(map(int,input().strip().split()))[:n] 
    i = 0   
    for i in range(n):
        flag = True
        if arr[i] != arr[n - i-1]:
            flag = chkpalin(arr,arr[i]) or chkpalin(arr,arr[n-i-1])
    
    if flag == True:
        print("YES")
    else:
        print("NO")
    t = t-1
        
        
        