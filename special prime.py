print("Special prime numbers")
from math import sqrt
#Given two numbers n and k, find whether there exist at least k Special prime numbers or not from 2 to n inclusively.
#A prime number is said to be Special prime number if it can be expressed as the sum of three integer numbers: two neighboring prime numbers and 1. For example, 19 = 7 + 11 + 1, or 13 = 5 + 7 + 1.
#Note:- Two prime numbers are called neighboring if there are no other prime numbers between them.

L = 2
n = int(input("n = "))
arr = []
for num in range(L,n,+1):
	if num>1:
		for i in range(2,num):
			if (num % i == 0):
				break
		else:
			arr.append(num)

print(arr)








import math
print("Marsenne Prime")

def prime_check(n):
	if n>1:
		for i in range(2,int(math.sqrt(n)+1)):
			if (n%i) == 0:
				return False
				break
		else:
			return True
#n = int(input("n = "))
#print(prime_check(n))

n = int(input("n = "))
a = int
arr = []
for i in range(2,int(math.sqrt(n))+1,+1):
	a = (2**i) -1
	if a>n:
		break
	arr.append(a)
#print(arr)

for j in arr:
	if prime_check(j) is True:
		print(j)
