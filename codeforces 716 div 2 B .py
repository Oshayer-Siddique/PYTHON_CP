t = int(input())
while t > 0:
    n,k = map(int,input().split())

    ans = (n**k) % ((10**9)+7)

    print(ans)

    t = t-1