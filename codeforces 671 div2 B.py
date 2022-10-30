#print("Codeforces 671 div 2 B")
t = int(input())
while(t > 0):
    x = int(input())
    ans = 0
    lth = 1
    p = 1
    while(x > 0):
        square_req = (lth*(lth+1))//2
        if (square_req > x):
            break
        else:
            x = x - square_req
            p = p * 2
            lth = lth + p
            ans = ans+1
    print(ans)
    t = t-1
