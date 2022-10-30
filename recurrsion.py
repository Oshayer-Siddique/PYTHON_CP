print("sum of list")


def sum_list(L):
    if len(L) == 1:
        return L[0]
    else:
        return L[0] + sum_list(L[1:])


L = [2, 2, 2, 2, 2]
print(sum_list(L))

print("harmonic series")


def harmonic_sum(n):
    if n == 1:
        return 1
    else:
        return 1 / n + harmonic_sum(n - 1)


n = int(input("n = "))
print(harmonic_sum(n))

print("call function")


def func(x):
    return x * (x + 1) % 11


x = 1
L = []
a = func(x)
a1 = func(func(x))
a2 = func(func(func(x)))
L.append(a)
L.append(a1)
L.append(a2)
print(L)


def fun(a, n):
    if n == 1:
        return a[0]
    else:
        x = fun(a, n - 1)
    if (x > a[n - 1]):
        return x
    else:
        return a[n - 1]


arr = [12, 10, 30, 50, 100]
print(fun(arr, 5))


def decreasing(n):
    if n == 0 or n < 0:
        print(n, end=", ")
        return
    else:
        print(n, end=", ")
        decreasing(n - 5)
        print(n, end=", ")


decreasing(16)

print("grid problem by recurssion")


def grid_path(n, m):
    if n == 1 or m == 1:
        return 1
    else:
        return grid_path(n - 1, m) + grid_path(n, m - 1)


n = int(input("n =  "))
m = int(input("m = "))
print(grid_path(n, m))

print("secret Origins")
print("General Onoroy Function")


def onoroy_value(num):
    bin_num = bin(num)
    count = 0
    for i in bin_num:
        if i == '1':
            count = count + 1
    return count


num = int(input("num = "))
print("Onoroy Value = ", onoroy_value(num))
a = onoroy_value(num)

while (True):
    if onoroy_value(num + 1) == a:
        break
    else:
        num = num + 1

print(num + 1)
print(onoroy_value(num + 1))

print("Number recurssion")


def func(n):
    if n == 1:
        return 0
    else:
        return 1 + func(n // 2)


n = int(input("n = "))
print(func(n))

print("String reverse by recurrsion")


def reverse(str):
    if len(str) == 0:
        return str
    else:
        return reverse(str[1:]) + str[0]


str = 'abcde'
print(reverse(str))

print("Palindrome check")


def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


s = str(input())
# print(reverse(s))

if reverse(s) == s:
    print("yes")
else:
    print("No")
print("Write a recursive function that, given a number n, returns the sum of the digits of the number")


def sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum(int(n / 10))


n = 123
print(sum(n))

print("Subsequence of string or not")


def stringtest(s1, s2, L):
    for i in s1:
        for j in s2:
            if i == j:
                L.append(i)
    return ''.join(L)


s1 = 'hac'
s2 = 'cathartic'
L = []
# print(stringtest(s1, s2, L))
s = stringtest(s1, s2, L) and s1
if len(s) == 0:
    print("no")
else:
    print("yes")
# print(s)
# Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
print("Leonardo Number")


def leonum(n):
    if n == 0 or n == 1:
        return 1
    else:
        return leonum(n - 1) + leonum(n - 2) + 1


n = int(input("n = "))
print(leonum(n))

print("Maximum elementin list with recurrsion")


def fun(a, n):
    if (n == 1):
        return a[0]
    else:
        x = fun(a, n - 1)
    if (x > a[n - 1]):
        return x
    else:
        return a[n - 1]

    # Driver code



arr = [12, 10, 30, 200, 50, 100]
print(fun(arr, 5))

print("McCarthy 91 function.")
def func(n):
  if n>100:
    return n-10
  else:
    return func(func(n+11))
n = int(input("n = "))
print(func(n))

