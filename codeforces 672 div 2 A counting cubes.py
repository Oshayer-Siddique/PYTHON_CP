#print("codeforces 672 div 2 A counting cubes")
t = int(input())
while(t>0):
    n = int(input())
    arr = arr = list(map(int,input().strip().split()))[:n]
    cur = 0
    for i in range(1,len(arr)):
        if arr[i-1]<=arr[i]:
            cur = cur+1
            break
    if cur == 1:
        print("YES")
    else:
        print("NO")
    t = t-1
