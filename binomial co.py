print("binomial co by another way(pascal triangle)")


def binomial_co(n, k):
    if k == 0 or k == n:
        return
    else:
        return binomial_co(n - 1, k - 1) + binomial_co(n - 1, k)


n = int(input("n = "))
k = int(input("k = "))

print(binomial_co(n, k))

print("Sum of squares of binomial coefficients")


def factorial(p):
    for i in range(1, p):
        p = p * i
    return p


n = int(input("n = "))

x = factorial(2 * n) / (factorial(n) * factorial(n))

print(int(x))

print("Maximum binomial coefficient term value")


def factorial(p):
    for i in range(1, p):
        p = p * i
    return p


n = int(input("n = "))


def max_binomial_co(n):
    if n % 2 == 0:
        return int(factorial(n) / (factorial(n // 2) * (factorial(n // 2))))
    elif n % 2 != 0:
        return int(factorial(n) / ((factorial((n - 1) // 2)) * (factorial((n + 1) // 2))))


print(max_binomial_co(n))

print("Maximum points of intersection n circles")


def max_point(n):
    return n * (n - 1)


n = int(input("n = "))
print(max_point(n))
