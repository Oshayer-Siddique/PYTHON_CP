t = int(input())
while t > 0:
    s = str(input())
    x = int(input())
    w = ['1'for i in range(len(s))]
    if s == '01':
        print('10')
    else:
        for i in range(0,len(s),+1):
            if s[i] == '0':
                if i-x>0:
                    w[i-x] = '0'
                elif i+x<len(s):
                    w[i+x] = '0'
        for i in range(len(s)):
            if s[i] == '1':
                if (i-x>=0 and w[i-x] == '1') or (i+x<len(s) and w[i+x] == '1'):
                    continue
                else:
                    print(-1)
    
            else:
                if (i-x>=0 and w[i-x] == '1') or (i+x<len(s) and w[i+x] == '1'):
                    print(-1)
            
        print(''.join(w))

        
    t = t-1