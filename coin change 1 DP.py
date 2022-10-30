def  count(S,n,w):
    a = [[0 for x in range(w+1)] for x in range(n)]
    for i in range(n):
        a[i][0] = 1
    
    for i in range(0,len(S),+1):
        for j in range(w+1):
            if S[i]>j:
                a[i][j] = a[i-1][j]
            else:
                a[i][j] = a[i-1][j] + a[i][j - S[i]]
    
    return a[n-1][w]
    

n,w  = map(int,input().split())
S = list(map(int,input().strip().split()))[:n]
if count(S,n,w) == 0:
    print("NO solution")
else:
    print("YES")
    print(count(S,n,w))

