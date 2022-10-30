
n = int(input())
def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return func(n-1) + (n-1)*func(n-2)

print(func(n))


print("With Dynamic Programme")
n = int(input())
def func1(n):
    dp = [0 for i in range(n+1)]
    for i in range(n+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        else:
            dp[i] = dp[i-1] + (i-1)*dp[i-2]
    return dp[n]

print(func1(n))