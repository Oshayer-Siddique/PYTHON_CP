n = int(input())

if  n == 2 or n == 3 :
    print("NO SOLUTION")
else:
    arr1 = []
    arr2 = []
    ans = []
    for i in range(1,n+1,+1):
        if i % 2 == 1:
            arr1.append(i)
        if i % 2 == 0:
            arr2.append(i)
    arr1.reverse()
    arr2.reverse()

    ans = arr1 + arr2

    print(*ans,sep = " ")
    
