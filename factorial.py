print("Sum of divisors of factorial of a number")

def factorial(p):
    for i in range(1,p):
        p = p*i
    return p

n = int(input("x = "))
sum  = 0
for i in range(1,factorial(n)+1,+1):
    if (factorial(n) % i) == 0:
        sum = sum + i

print(sum)


print("Count Divisors of Factorial")
def factorial(p):
    for i in range(1,p):
        p = p*i
    return p
n = int(input("n = "))
count = 0
for i in range(1,factorial(n)+1,+1):
    if factorial(n) % i == 0:
        count = count + 1

print(count)

import math
def trailing_zero(n):
    count = 0
    i = 5
    while(i<=n):
        count = count+math.floor(n/i)
        i = i*5
    return int(count)

n = int(input("n = "))
print(trailing_zero(n))

import math
def max_power(p):
    count = 0
    j = max_prime_factor(n)
    while (j<=p):
        count = count+math.floor(p/j)
        j = j*max_prime_factor(n)

    return int(count)

def max_prime_factor(n):
    maxprime = -1
    while n%2 == 0:
        maxprime = 2
        n = n/2

    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i == 0:
            maxprime = i
            n = n/i

    if n>2:
        maxprime = n
    return int(maxprime)


p = int(input("p = "))
n = int(input("n = "))
print(max_power(p))


print("Find all factorial numbers less than or equal to n")

import math
print("Find all factorial numbers less than or equal to n")
f = 1
k = int(input("k = "))
for i in range(1,int(math.sqrt(k))):
    f = f*i
    if f > k:
        break
    print(f)

print("Count digits in a factorial | Set 1")
import math
n = int(input("n = "))
f = 1
for i in range(1,n+1,1):
    f = f * i
    c = f

def count_digits():
    return math.floor(math.log(c,10)) + 1


print(count_digits())

print("find all prime factors")
def prime_factor(n):
	while(n%2 == 0):
		print(2)
		n = n/2
	for i in range(3,int(n//2),+1):
		while(n % i == 0):
			n = n/i
			print(i)

n = int(input("n = "))
print(prime_factor(n))

