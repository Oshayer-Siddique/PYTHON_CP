print("fibonacci")
print("0")
print("1")
a = 0
b = 1
n = 10
for i in range(2, n + 1):
    c = a + b
    a = b
    b = c
    print(c, ",")

import math

print("check the number is it fibonacci or not")

n = int(input("n = "))

x = (math.sqrt(5 * n * n + 4))
y = (math.sqrt(5 * n * n - 4))
if math.floor(x) == math.ceil(x):
    print("yes", n, "is a fibonacci number")
elif math.floor(y) == math.ceil(y):
    print("yes", n, "is a fibonacci number")
else:
    print("No")

print("Even Fibonacci Numbers Sum")
n = int(input("n = "))
f0 = 0
f1 = 1

for i in range(2, n + 1):
    f2 = f0 + f1
    f0 = f1
    f1 = f2
    if f2 % 2 == 0:
        print(f2)
    elif f2 >= n:
        break

print("fibonacci traingle")


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("n = "))
print(fibonacci(n))

print("fibonacci  series")


def fibonacci(n):
    if n == 0:
        return 0
    elif (n == 1 or n == 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


nterms = int(input("nterms = "))
if nterms < 0:
    print("give a positve intager")
else:
    for i in range(nterms):
        print(fibonacci(i))
