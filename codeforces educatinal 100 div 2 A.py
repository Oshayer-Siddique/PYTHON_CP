t = int(input())
while t > 0:
    a,b,c = map(int,input().split())
    sum = a+b+c
    val = sum//9
    if  sum % 9 != 0 or a<val or b<val or c < val:
        print("NO")
    else:
        print("YES")
    t = t-1
    
 


