t = int(input())
while t > 0:
    a,b,c,d = map(int,input().split())
    count = 0
    if b  > a:
        count+=1
    if c > a:
        count += 1
    if d > a:
        count+=1
    
    print(count)
    t = t-1
