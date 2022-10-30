t = int(input())
while t > 0:
    n,k1,k2 = map(int,input().split())
    w , b  = map(int,input().split())
    flag1 = 0
    flag2 = 0
    if 2 *w <= (k1+k2):
        flag1 = 1
    if 2 * b <= (2*n - k1 - k2):
        flag2 = 1


    if flag1 == 1 and flag2 == 1:
        print("YES")
    else:
        print("NO")
    t = t-1