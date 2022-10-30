t = int(input())
while(t>0):

    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    flag = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                flag = 1
                break
    if flag == 1:
        print("YES")
    else:
        print("NO")
    t = t-1      
          
                    