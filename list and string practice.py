print("decimal to binary")

def decimaltobinary(num):
	if num > 1:
		decimaltobinary(num//2)
	print(num % 2,end = '')

num = 24
decimaltobinary(num)

print("decimal ti octal")

def decimaltooctal(num):
	if num > 1:
		decimaltooctal(num//8)
	print(num % 8,end = '')

num = int(input("dec = "))
decimaltooctal(num)

print("binary to decimal")
num = list(input())
n = len(num)
sum = 0
for i in range(n):
	digit = num.pop()
	if digit == '1':
		sum = sum + pow(2,i)

print(sum)



print("Array simulation 1133")
def add(L):
	L1 = []
	for i in L:
		L1.append(i+D)
	return L1
D = int(input("D = "))

def product(L):
	L1 = []
	for i in L:
		L1.append(i*M)

	return L1
M = int(input("M = "))

def divide(L):
	L1 = []
	for i in L:
		L1.append(i//K)
	return L1
K = int(input("K = "))

def reverse(L):
	return L[::-1]



array = [1,2,3,4,5]
print(product(array))
print(add(array))
print(divide(array))
print(reverse(array))
