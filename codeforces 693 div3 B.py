t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    a = arr.count(1)
    b = arr.count(2)
    
    
    
    if sum(arr) % 2 != 0:
        print("NO")
    elif a == 0 and b % 2 == 1:
        print("NO")
    elif b == 0 and a % 2 == 1:
        print("NO")
    elif a % 2 == 0 and (2*b) % 2 == 0:
        print("YES")
    else:
        print("NO")
    t = t-1
