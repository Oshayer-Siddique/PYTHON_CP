t = int(input())
while t > 0:
    x,y = map(int,input().split())
    s = str(input())
    R = s.count('R')
    L = s.count('L')
    U = s.count('U')
    D = s.count('D')
    if (x > 0 and y == 0) and (R >= abs(x)):
        print("YES")
    elif (x < 0 and y == 0) and ( L >= abs(x)):
        print("YES")
    elif (y > 0 and x == 0) and (U >= abs(y)):
        print("YES")
    elif (y < 0 and x == 0) and (D >= abs(y)):
        print("YES")
    elif (x < 0 and y >0) and (L >= abs(x) and U >= abs(y)):
        print("YES")
    elif (x > 0 and y >0) and (R>= abs(x) and U >= abs(y)):
        print("YES")
    elif (x < 0 and y < 0 ) and (L >= abs(x) and D >= abs(y)):
        print("YES")
    elif (x > 0 and y < 0) and R >= abs(x) and D>= abs(y):
        print("YES")
    else:
        print("NO")

    t = t-1
