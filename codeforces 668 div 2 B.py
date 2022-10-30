t = int(input())
while(t>0):
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    sum = ans = 0
    for i in range(n):
        sum = sum+arr[i]
        ans = min(ans,sum)
 
    print(abs(ans))
    t = t-1
    
    

