t = int(input())
while t > 0:
    n,p,q = map(int,input().split())
    s = str(input())
    def count_function(s,a,b):
        cnt = 0
        stor = []
        i = 0
        while i < len(s):
            if s[i] == a:
                cnt+=1
            if s[i] == b:
                cnt = 0
            i+=1
            stor.append(cnt)
    
        u = len(stor)
        final = []
        for i in range(len(stor)-1):
            if stor[i+1] == 0:
                final.append(stor[i])
    
        if stor[-1] != 0:
            final.append(stor[-1])

        last = []
        for i in range(len(final)):
            if final[i] != 0:
                last.append(final[i])
    
        return last


#print(count_function(s,'0','1'))
#print(count_function(s,'1','0'))
    ans1 = 0
    x = len(count_function(s,'0','1'))
    y = len(count_function(s,'1','0'))
    m=  min(x,y)
    sum1 = 0
    if len(count_function(s,'0','1')) == m:
        sum1 = sum(count_function(s,'0','1'))
    else:
        sum1 = sum(count_function(s,'1','0'))
    sum2 = 0
    if len(count_function(s,'0','1')) != m:
        sum2 = sum(count_function(s,'0','1'))
    else:
        sum2 = sum(count_function(s,'1','0'))
#print(sum1,sum2)
    ans1 = ((p*sum1) + (m*q)) + (p*sum2) + q

#print(x,y)


    ans = 0
    if q >0:
        ans = (p*n) + (q*n)
    else:   
        ans = ans1


    print(ans)
    t = t-1