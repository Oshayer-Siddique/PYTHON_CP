import math
n = int(input())

for i in range(1,n+1,+1):
    j = 5*i+3
    
    k = 8*i + 1

    if math.gcd(j,k) > 1:
        print(j,k)
        print(i)
        print(math.gcd(j,k))


