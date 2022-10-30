t = int(input())
while t > 0:
    n = int(input())
    s = str(input())
    if s[0] == '2' and s[-1] == '0' and s[-2] == '2' and s[-3] == '0':
        print("YES")
    elif s[0] == '2' and s[1] == '0' and s[2] == '2' and s[-1] == '0':
        print("YES")
    elif s[0] == '2' and s[1] == '0' and s[2] == '2' and s[3] == '0':
        print("YES")
    elif s[-1] == '0' and s[-2] == '2' and s[-3] == '0' and s[-4] == '2':
        print("YES")
    elif s[0] == '2' and s[1] == '0' and s[-1] == '0' and s[-2] == '2':
        print("YES")
    else:
        print("NO")
    
    t = t-1