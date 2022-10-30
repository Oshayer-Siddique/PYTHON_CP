t = int(input())
while(t>0):
    n = int(input())
    s = str(n)

    maximum = int(max(s))
    lth = len(s)
    #print(lth)
    if lth == 2:
        another = 3
    elif lth == 3:
        another = 6
    elif lth == 4:
        another = 10
    elif lth == 1:
        another = 1

    ans = 10*(maximum-1) + another
    print(ans)
    t = t-1
    
