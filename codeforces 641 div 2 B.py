t = int(input())
while t > 0:
    n = int(input())
    arr = [0] + list(map(int,input().strip().split()))[:n]
    stor = []
    f = [1 for i in range(n+1)]
    for i in range(1,n+1,+1):
        for j in range(i*2,n+1,+i):
            if arr[j]  > arr[i]:
                f[j] = max(f[j],f[i]+1)
                stor.append(f[j])
 
    if len(stor) == 0:
        print(1)
    else:
        print(max(stor))
    t = t-1
            
      
