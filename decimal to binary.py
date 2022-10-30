n = int(input())

arr = []
if n == 0:
    print(0)
else:
    while(n != 0 ):
    
        rem = n%2
        n //=2
    
    
        arr.append(rem)
    

    arr.reverse()
    print(*arr,sep="")
    
