print("Modular multiplicative inverse")


def modolu(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x

    return 1


a = int(input("a = "))
m = int(input("m = "))
print(modolu(a, m))
