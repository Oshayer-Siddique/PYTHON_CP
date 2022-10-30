
n = int(input())
arr = list(map(int,input().strip().split()))[:n]
m = int(input())
for i in range(m):
    u , v = map(int,input().split())   
    suf_sm = 0 
    ans = 0
    for i in range(v,u-1,-1):
        ans = ans + (arr[i] * (suf_sm + arr[i]))
        suf_sm += arr[i]

    print(ans)
    
    
    
        
    
    
    