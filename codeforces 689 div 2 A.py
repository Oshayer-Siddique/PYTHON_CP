t = int(input())
while t>0:
    n,k = map(int,input().split())
    for i in range(n):
        if i % 3 == 0:
            print('a',end="")
        elif i % 3 == 1:
            print('b',end="")
        else:
            print('c',end="")
    print('\t')
    t = t-1