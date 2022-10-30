t = int(input())

while(t>0):
    n ,x = map(int,input().split())
    arr1 = list(map(int,input().strip().split()))[:n]
    arr2 = list(map(int,input().strip().split()))[:n]
    arr1.sort()
    arr2.sort()
    arr2.reverse()
    for i in range(n):
        for j in range(n):
            if arr1[i] + arr2[j] > x:
                print("No")
            else:
                print("Yes")
    t = t-1

    
    