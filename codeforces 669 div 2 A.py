t = int(input())
while(t>0):
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    cnt_0 = arr.count(0)
    if cnt_0 >= n/2:
        print(cnt_0)
        for i in range(cnt_0):
            print(0,end=" ")
    elif cnt_0 < n/2:
        print(arr.count(1)-arr.count(1)%2)
        for i in range(arr.count(1)-arr.count(1)%2):
            print(1,end=" ")
    print("\t")
    t = t-1

    
