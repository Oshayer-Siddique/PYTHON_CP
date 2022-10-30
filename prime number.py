print("Efficient program to print all prime factors of a given number")
import math
def prime_factor(n):

    while n % 2 == 0:
        print(2)
        n = n/2

    for i in range(3,int(math.sqrt(n))+1,+2):

        while n % i == 0:
            print(i)
            n = n / i

    if n > 2:
        print(n)

n = int(input("n = "))
prime_factor(n)

print("prime number and fibonacci")
def fibonacci(n):
    a = 0
    b = 1
    for i in range(2,n+1):
        c = a+b
        a = b
        b = c
        print(c)

n = int(input("n = "))
print("0")
print("1")
print(fibonacci(n))

print("prime numbers")
max = int(input("max = "))
min = int(input("min = "))
