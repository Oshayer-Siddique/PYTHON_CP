t = int(input())
while t > 0 :
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    flag = 0
    cur1 = 0
    cur2 = 0
    for i in range(n):
        if arr[i] != 1:
            flag = 1
            break
    for i in range(n):
        if arr[i] > 1 and i % 2 == 0:
            cur1 = 1
            break
        elif arr[i] > 1 and i % 2 == 1:
            cur2 = 1
            break
    if cur1 == 1:
        print("First")
    elif cur2 == 1:
        print("Second")
    elif flag == 0:
        if n % 2 == 1:
            print("First")
        else:
            print("Second")

    t = t-1
