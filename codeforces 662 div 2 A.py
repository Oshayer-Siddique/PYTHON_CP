t = int(input())
while t > 0:
    def func(n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return 2 + (func(n-2)-1)

    n = int(input())
    print(func(n))
    t = t-1
