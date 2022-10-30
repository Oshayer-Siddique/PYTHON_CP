n,x = map(int,input().split())
arr = list(map(int,input().strip().split()))[:n]
flag = 0
a,b = 0, 0 
for i in range(n-1):
    for j in range(i+1,n,+1):
        if arr[i] + arr[j] == x:
            a = i
            b = j
            flag = 1
            break

if flag == 1:
    print(a+1,b+1)
else:
    print("IMPOSSIBLE")