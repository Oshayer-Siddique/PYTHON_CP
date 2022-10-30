print("Moodular exponential")


def mod_pow(x, n, M):
    if n == 0:
        return 1
    elif (n % 2) == 0:
        res = pow(x, n / 2) % M
        return (res * res) % M
    else:
        return (pow(x, 1) % M * pow(x, n - 1) % M) % M


x = int(input("x = "))
n = int(input("n = "))
M = int(input("M = "))
print(mod_pow(x, n, M))

print("another way")
x = int(input("x = "))
n = int(input("n = "))
M = int(input("M = "))
p = (x ** n) % M
print(p)
