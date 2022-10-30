t = int(input())
while(t>0):
    n,m = map(int,input().split())
    arr = []
    for k in range(n):
        a = list(map(int,input().split()))[:m]
        arr.append(a)

    for i in range(n):
        for j in range(m):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                if arr[i][j] % 2 == 0:
                    arr[i][j] = arr[i][j] + 1
            elif (i % 2 == 1 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 1):
                if arr[i][j] % 2 == 1:
                    arr[i][j] = arr[i][j]+1
            
            
            print(arr[i][j],end=" ")
        print()
  
    t = t-1
    
    
     