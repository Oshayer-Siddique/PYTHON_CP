import math
t = int(input())
while t > 0:
    n,k = map(int,input().split())
    if k > n:
        ans = math.ceil(k/n)
    elif n == k:
        ans = 1
    elif n > k:
        if n % k == 0:
            ans = 1
        else:
            ans = 2

    print(ans)
    t = t-1
#story_times Barcelonavsrealmadrid
