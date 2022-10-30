t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    one = 0
    three = 0
    for i in range(n):
        if arr[i] == 1:
            one += 1
        elif arr[i] == 3:
            three+= 1

    total = one+ three

    print(total)
    t = t-1