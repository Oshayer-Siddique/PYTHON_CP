t = int(input())
while t > 0:
    n = int(input())
    if n == 1:
        print(9)
    elif n ==2:
        print(98)
    else:
        print("989",end="")
        for i in range(1,n-2,+1):
            print((i-1)%10,end="")
        print("\t")
    t = t-1