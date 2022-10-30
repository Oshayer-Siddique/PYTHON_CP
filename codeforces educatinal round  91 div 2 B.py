t = int(input())
while t > 0:
    s = str(input())
    R = s.count('R')
    P = s.count('P')
    S = s.count('S')
    A = max(R,P,S)
    n = len(s)
    if A == R:
        for i in range(n):
            print('P',end="")
    elif A == P:
        for j in range(n):
            print('S',end="")
    elif A == S:
        for k in range(n):
            print('R',end="")
    print('\t')
    t = t-1