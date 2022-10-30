
def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif arr[n] != -1:
        return arr[n]
    else:
        return func(n-1) + 2*func(n-2)
arr = [-1]*1000
n = int(input())
print(func(n))