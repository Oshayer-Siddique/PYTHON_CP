print("Special Series Sum")
print("1 + (1+2) + (1+2+3) + (1+2+3+4) + …… + (1+2+3+4+…+n)")
n = int(input("n = "))
sum = 0
for i in range(0,n+1,+1):
    for j in range(0,i+1,+1):
        sum +=j

print(sum)
print("Sum of the Series 1/(1*2) + 1/(2*3) + 1/(3*4) + 1/(4*5) + . . . . .")
n = 10
sum = 0
for i in range(1,n+1,+1):
    sum = sum + 1/(i*(i+1))

print(sum)

print("Sum of the series 1 + (1+3) + (1+3+5) + (1+3+5+7) + …… + (1+3+5+7+…+(2n-1))")
n = 5
sum = 0
for i in range(0,n+1,+1):
    k = 1
    for j in range(1,i+1):
        sum = sum+k
        k = k+2

print(sum)

print("Sum of the series 2 + (2+4) + (2+4+6) + (2+4+6+8) + …… + (2+4+6+8+….+2n)")
n = 5
sum = 0
for i in range(0,n+1,+1):
    k = 0
    for j in range(0,i+1):
        sum = sum + k
        k = k+2
print(sum)

print("Sum of the series 1.2.3 + 2.3.4 + … + n(n+1)(n+2)")
n = 3
sum = 0
for i in range(0,n+1,+1):
    sum  = sum + (i*(i+1)*(i+2))

print(sum)

print("Sum of the Series 1 + x/1 + x^2/2 + x^3/3 + .. + x^n/n")
x = int(input("x = "))
n = int(input("n = "))
sum = 0
for i in range(1,n+1,+1):
    sum = sum + ((x**i)/i)

print(sum+1)




print("Sum of series: 1 – x^2/2! + x^4/4! -…. upto nth term")
import math
x = 9
n = 10
sum = 1
y = 2
term = 1
for i in range(1,n,+1):
    fact = 1
    for j in range(1,y+1):
        fact = fact * j
    term = term*(-1)
    m = term*(math.pow(x,y))/fact
    sum = sum+m
    y = y+2

print(sum)

print("series 1")
n = int(input("n = "))
sum = 0
for i in range(1,n):
	for j in range(1,(i*3)+1,+1):
		sum = sum + j

#print(sum+1)


sum1 = 0
for p in range(1,n):
	for q in range(1,(p*3)-2,+1):
		sum1 = sum1 +q

#print(sum1+1)

series_sum = sum-sum1
print(series_sum)

print("sum of series by recurssion")
def sum(n):
	if n == 1:
		return 1
	else:
		return  sum(n-1) + n
n = int(input())
print(sum(n))

print("Padovan series")
def padovan(n):
	if (n == 0 or n == 1 or n == 2):
		return 1
	else:
		return padovan(n-2)+padovan(n-3)

n = int(input("n = "))
print(padovan(n))
