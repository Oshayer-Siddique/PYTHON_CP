
import math
t = int(input())
while t > 0:
    n = int(input())
    miner = []
    diamond = []
    for i in range(2*n):
        m,d = map(int,input().split())
        if m == 0:
            miner.append(abs(d))
        elif d == 0:
            diamond.append(abs(m))


    miner.sort()
    diamond.sort()
    temp = 0
    ans = 0
    for i in range(len(miner)):
        temp = (miner[i]*miner[i]) + (diamond[i]*diamond[i])
        ans =  ans + math.sqrt(temp)

    print(ans)
    t = t-1


