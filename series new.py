import math
print("Juggler Sequence")

a = int(input("a =  "))
while (a!=1):
    b = 1
    if (a%2 == 0):
        b = int((math.floor(a))**(0.5))
    else:
        b = int((math.floor(a))**(1.5))
    a = b
    print(b)

print("fibonacci")
print("0")
print("1")
a = 0
b = 1
n = 10
for i in range(2,n+1):
    c = a+b
    a = b
    b = c
    print(c,",")

print("Padovan sequence")
print("1")
print("1")
print("1")
P0 = 1
P1 = 1
P2 = 1
n = 7
for i in range(2,n):
    P3 = P1 + P0
    P0 = P1
    P1 = P2
    P2 = P3
    print(P3)



print("Newman-Conway Sequence")
def sequence(n):
    if n == 1 or n == 2:
        return 1
    else:
        return sequence(sequence(n-1)) + sequence(n-sequence(n-1))

n = 10
print(sequence(n))


print("Hello")
def greet():
    print("hello")
    greet()

greet()

print("fibonacci by recursion")
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n  = int(input("n = "))
print(fibonacci(n))

print("padovan series")
