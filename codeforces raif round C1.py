t = int(input())
while(t>0):
    s = str(input())
    ans = 0
    for i in s:
        if i == 'B' and ans!= 0:
            ans = ans-1
        else:
            ans = ans+1

    print(ans)
    t = t-1