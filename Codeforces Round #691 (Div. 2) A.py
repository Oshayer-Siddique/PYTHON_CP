t = int(input())
while t > 0:
    n = int(input())
    a = input()
    b = input()
    x = 0
    y = 0
    for i in range(n):
        if a[i] > b[i]:
            x = x+1
        elif a[i] < b[i]:
            y = y+1
    if x > y:
        print("RED")
    elif x < y:
        print("BLUE")
    else:
        print("EQUAL")

    t = t-1

