import math
print("light oj 1045 ")
def factorial(n):
    for i in range(1,n):
        n = n*i
    return n
n = int(input("n = "))
#print(factorial(n))


def decimaltoxbase(p):
	if p>1:
		decimaltoxbase(p//x)
	print(p%x,end='')
p = factorial(n)
x = int(input("x = "))
decimaltoxbase(p)


t = int(input("t = "))
a = math.log(t,10)
b = (math.floor(a))+1
print(b)

def large_divission(a,b):
	for c in range(a+1):
		if c*b == a:
			return c


a = int(input("a = "))
b = int(input("b = "))
print(large_divission(a,b))

num = input("Enter a number = ")
if num == num[::-1]:
	print("Yes its a palindrome")
else:
	print("No, its not a palindrome")


def find_zero(L):
	for i in range(len(L)):
		if L[i] == 0:
			return i
	return None
L = []

path = [1,1,1,0,1,1]
start_pos = [2,2]
count = 0
for i in range(len(path)):
	if path[i] == 1:
		count = count+1
	else:
		break
#print(count)
print("starting position = ",start_pos)

first_pos = (start_pos[0],start_pos[1]+count)
print("first position = ",first_pos)


a = find_zero(path)
print(a)
x = path.count(1::a)
