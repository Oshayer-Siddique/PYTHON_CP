import math
t = int(input())
while t > 0:
    a,b = map(int,input().split())
    if a == b:
        ans = 0
        i = 0
    else:
        ans = abs(a - b)
        i = 0
        flag = max(a,b)
        while i <= flag:
            if math.gcd(a,b) == ans:
        
                break
            else:
                a = a+1
                b = b+1
                i = i+1



    print(ans,i)

    t = t-1