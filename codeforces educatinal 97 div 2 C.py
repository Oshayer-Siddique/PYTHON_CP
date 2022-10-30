t = int(input())
while(t>0):
    n = int(input())
    s = str(input())
    ans = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            ans = ans+1
    
    print((ans+1)//2)

    t = t-1