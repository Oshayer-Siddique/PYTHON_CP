

#Using Recurssion

'''def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))'''

# using dynamic programming
n = int(input())
f = [0,1]

for i in range(2,n+1,+1):
    f.append(f[i-1] + f[i-2])

print(f[n-1])
