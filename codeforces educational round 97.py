t = int(input())
while(t>0):
    l,r = map(int,input().split())
    if (r-l) < l:
        print("YES")
    
    else:
        print("NO")
    t = t-1
