t = int(input())
while(t>0):
    n ,m = map(int,input().split())
    arr = list(map(int,input().strip().split()))[:n]
    sum = 0
    for i in range(1,len(arr)+1,+1):
        for j in range(i,len(arr)+1,+1):
            sum = sum+((arr[j-1])/j)
    if round(sum) == m:
        print("YES")
    else:
        print("NO")
    t = t-1