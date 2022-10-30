t = int(input())
while t > 0:
    s = str(input())
    if s[0] == ')' or s[-1] == "(":
        print("NO")
    else:

        count1 = 0
        count2 = 0
        for i in s:
            if i == '(':
                count1 = count1+1
            elif i == ')':
                count2 = count2+1
        #print(count1,count2)
        if count1 > count2:
            s = s.replace("?",")",count1-count2)
        elif count2 > count1:
            s = s.replace("?","(",count2-count1)
        c1=0
        c2=0
        c3=0
        for j in s:
            if j == "(":
                c1 = c1+1
            elif j == ")":
                c2 = c2+1
            elif j == "?":
                c3 = c3+1
        if (c1 == c2) and (c3 % 2 == 0):
            print("YES")
        else:
            print("NO")
        #print(s)
    t = t-1