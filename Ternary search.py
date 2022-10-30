s = str(input())
def function(s,x):
    cnt = 0
    stor = []
    i = 0
    while i < len(s):
        if s[i] == x:
            cnt+=1
        else:
            cnt = 0
 
        i = i+1
        stor.append(cnt)
    
    n = len(stor)
    final = []
 
    for i in range(len(stor)-1):
        if stor[i+1] == 0:
            final.append(stor[i])
    
    if stor[-1] != 0:
        final.append(stor[-1])
    ans = max(final)
 
    return ans
 
 
#print(function(s, x))
 
ans1 = function(s,'1')
ans2 = function(s, '2')
ans3 = function(s, '3')
#ans4 = function(s, 'T')
 
print(max(ans1, ans2, ans3))