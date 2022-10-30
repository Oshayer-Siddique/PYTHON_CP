t = int(input())
while(t>0):
    s = str(input())
    total = 0
    t1 = 0
    t2 = 0
    for i in s:
        if i == '(':
            t1 = t1+1
        if i == '[':
            t2 = t2+1
       
        if i == ')':
            if t1 > 0:
                total = total+1
                t1 = t1-1
        if i == ']':
            if t2>0:
                total = total+1
                t2 = t2-1
 
    print(total)
    t = t-1