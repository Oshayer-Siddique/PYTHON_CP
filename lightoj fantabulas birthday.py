
from math import ceil, sqrt
import math
t = int(input())
for i in range(1,t+1,+1):
    n = int(input())
    row,col = 0,0
    a = math.ceil(sqrt(n))
    b = math.floor(sqrt(n))
    dif1 = abs(a**2 - n)
    dif2 = abs(n - b**2)
    closestsqr = 0
    if dif1 < dif2 :
        closestsqr = a**2
    else:
        closestsqr = b**2




    if a % 2 == 1:
        if dif1 < dif2:
            row = a
        elif dif1 == dif2:
            if n % 2 == 1:
                col = 1
                row = a
            else:
                row = 1
                col = a
        
        else:
            col = a
        
        
   

    elif a % 2 == 0:
        if dif1 < dif2:
            col = a
        elif dif1 == dif2:
            if n % 2 == 0:
                row = 1
                col = a
            else:
                row = a
                col = 1
            
        else:
            row = a
        
    if col== 0:
        if n > closestsqr:
            col = abs(n - closestsqr)
        else:
            col = abs(closestsqr - n + 1)
    elif row == 0:
        if n  < closestsqr:
            row = abs(closestsqr - n + 1)
        else:
            row = abs(n - closestsqr)    
        
        
        
    #print(closestsqr)
    print(f"Case {i}: {col} {row}")
    
    
    