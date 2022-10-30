t = int(input())
while t > 0:
    n = int(input())
    flag = 0
    y = 0
    for i in range((n//2020) + 1):
        
        if (n - 2021*y) % 2020 == 0:
            flag = 1
            break
        y = y+1
    x = (n - 2021*y)//2020
    if x < 0 or y < 0:
        print("NO")
    else:
        print("YES")
    t = t-1
 
