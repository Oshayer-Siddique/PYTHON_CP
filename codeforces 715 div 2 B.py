u = int(input())
while  u > 0:
    n = int(input())
    s = str(input())
    flag = 0
    t ,m = 0,0
    for i in range(n):
        if s[i] == 'T':
            t += 1
        else:
            m += 1
        if m > t:
            flag = 1
            break
    cnt1,cnt2 = 0,0
    if n % 3 != 0:
        flag = 1
    elif 2*m != t:
        flag = 1
    
    else:
        for i in range(n-1,-1,-1):
            if s[i] == 'T':
                cnt1 += 1
            elif s[i] == 'M':
                cnt2 += 1
        
            if cnt2 > cnt1:
                flag = 1
                break
    
    if flag == 1:
        print("NO")
    else:
        print("YES")
                
            

    u = u-1