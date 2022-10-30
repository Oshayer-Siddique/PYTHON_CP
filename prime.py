import math
t  = int(input())
while t > 0:
    n = int(input())
    last = math.ceil(math.sqrt(n))
    flag = 0
    if n == 1:
        flag = 1
    elif n == 2:
        flag = 0
    elif n % 2 == 0:
        flag = 1
    else:
        for i in range(3,last,+2):
            if n % i == 0:
                flag = 1
                break
    if flag == 0:
        print("Prime")
    else:
        print("NOT prime")
    t = t-1
    