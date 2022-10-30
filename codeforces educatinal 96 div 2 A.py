t = int(input())
while(t>0):
    n = int(input())
    flag = 0
    y = 0
    z = 0
    while(True):
    
        while(True):
            if (n - 5*y - 7*z) % 3 == 0:
                flag = 1
                break
        
            z = z+1
        if flag == 1:
            break
        y = y+1
    x = (n - 5*y - 7*z)//3
    if n == 5:
        print(0,1,0)
    elif n == 8:
        print(1,1,0)
    elif n == 11:
        print(2,1,0)
    
    elif x < 0 or y < 0 or z < 0:
        print(-1)
    
    else:
        print(x,y,z)
    t = t-1

        
          
            
        

        


