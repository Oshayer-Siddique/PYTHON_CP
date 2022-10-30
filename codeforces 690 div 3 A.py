t = int(input())
while t >0:
    n = int(input())
    arr = [0]+ list(map(int,input().strip().split()))[:n]
    a = str(arr[(n//2)+1])
    if n % 2 == 1:
        for i in range(1,n//2+1,+1):
            print(arr[i],arr[-i],end=" ")
        print(a,end=" ")
    elif n % 2 == 0:
        for i in range(1,n//2+1,+1):
            print(arr[i],arr[-i],end=" ")
    print("\t")
    t = t-1
