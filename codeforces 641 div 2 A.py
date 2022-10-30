print("codeforces 641 div 2 A")

def func(n):
    for i in range(2,n+1,+1):
        if n % i == 0:
            return i


def final(n,k):
    for i in range(1,k+1,+1):
        f = func(n)+n
        n = f
    return f

t = int(input())
for i in range(t):
    n, k = map(int,input().split())
    print(final(n,k))
