t = int(input())
while t > 0:
    n = int(input())
    flag = 0
    while(n%2 == 0):
        n = n //2

    if n == 1:
        print("NO")
    else:
        print("YES")
    t = t-1
    



        