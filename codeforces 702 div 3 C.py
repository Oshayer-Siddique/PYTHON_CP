clist=[0]*10001
for i in range(1,10001):
    clist[i]=i*i*i
cubes=set(clist[1:])
 
for _ in range(int(input())):
    n=int(input())
    flag=0
    for i in range(1,10001):
        find=n-clist[i]
        
        if find in cubes:
            flag=1
        
    if flag == 1:
        print("YES")
    else:
        print('NO')

