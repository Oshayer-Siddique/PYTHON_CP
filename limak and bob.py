a,b = map(int,input().split())
flag = 0
for i in range(1,100,+1):
    a = a * 3
    b = b * 2
    
    if a > b:
        flag = 1
        break

if flag == 1:
    print(i)
    
    