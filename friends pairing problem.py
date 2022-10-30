#using recurrsion
def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return func(n-1) + (n-1) * func(n-2)

n =int(input())
print(func(n))

#using dynamic

n = int(input())
f = [0 for i in range(n+1)]
for i in range(1,n+1,+1):
    if i == 1:
        f[i] = 1
    elif i == 2:
        f[i] = 2
    else:
        f[i] = f[i-1] + (i-1)*f[i-2]

print(f[n])
        