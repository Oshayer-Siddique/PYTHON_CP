import math
print("Find x and y satisfying ax + by = n")
n = int(input("n = "))
a = int(input("a = "))
b = int(input("b = "))
for y in range(n+1):
    if ((n-b*y)%a == 0):
        print("y = ",y)
        print("x = ",(n-b*y)//a)

print("Program for dot product and cross product of two vectors")
vec_A = [3,-5,4]
vec_B = [2,6,5]
n = len(vec_A)
product = 0
for i in range(0,n):
    product = product + vec_A[i] * vec_B[i]
print("scaler product = ",product)

print("computational geo")
L = [[0,0],[1,1],[2,2],[3,5],[4,5]]

def slope(Lj,Li):
	return (Lj[1]-Li[1])/(Lj[0]-Li[0])

L = [[0,0],[1,1],[2,2],[3,5],[4,5]]

Lj = L[0]
Li = L[1],L[2],L[3]
print(slope(Lj,Li))


Lj = L[0]
Li = L[2]
print(slope(Lj,Li))

Lj = L[0]
Li = L[3]
print(slope(Lj,Li))

Lj = L[0]
Li = L[4]
print(slope(Lj,Li))

print("LCM and GCD")
def lcm(x,y):
	if x>y:
		L = x
	else:
		L = y
	while(True):
		if(L%x==0 and L%y==0):
			break
		else:
			L = L + 1
	return L

def product(x,y):
	return x*y

def gcd(x,y):
	return product(x,y)/lcm(x,y)

x = int(input("x = "))
y = int(input("y = "))
print(lcm(x,y))
print(gcd(x,y))


print("matrix addition")
X = [[1,2,5],
		[12,4,6],
		[10,12,5]]

Y = [[0,5,2],
		[1,5,8],
		[1,6,4]]

sum = [[0]*3 for m in range(3)]
for i in range(len(X)):
	for j in range(len(X)):
		sum[i][j] = X[i][j]+Y[i][j]

for r in sum:
	print(r)
