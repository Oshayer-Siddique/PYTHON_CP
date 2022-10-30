t = int(input())
while(t>0):
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    arr.reverse()
    print(*arr,sep=' ')
    t = t-1