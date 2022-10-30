y,b,r = map(int,input().split())
mini = min(y,b,r)
if y == b == mini and mini != r:
    ans = 3* mini
elif y == b == r:
    ans = mini + mini-1 + mini-2
 
elif y == mini:
    if r - y >= 2:
        y = mini
        b = y + 1
        r = y+ 2
        ans = y + b + r
    elif r - y < 2:
        ans = (3 * r) - 3
 
elif b == mini:
    if r - b >= 1:
        y = mini -1
        b = mini
        r = mini+1
        ans = y + b + r
    else:
        ans = (mini-1)*3
 
elif r == mini:
    ans = (3*mini) - 3
    
 
print(ans)
