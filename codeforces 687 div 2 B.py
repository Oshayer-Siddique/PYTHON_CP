t = int(input())
while t > 0:

    n = int(input())
    for i in range(n):
        for j in range(n):
            if i == j:
                print("1 ", end="")
            elif i + 1 == j:
                print("1 ", end="")
            elif i == (n - 1) and j == 0:
                print("1 ", end="")
            else:
                print("0 ", end="")

        print("\r")

    print()
    t = t - 1
