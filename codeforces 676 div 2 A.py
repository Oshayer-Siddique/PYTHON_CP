t = int(input())
while(t>0):
 
    a,b = map(int,input().split())
    x = a & b
    ans = (a^x)+(b^x)
    print(ans)
    t = t-1
   
