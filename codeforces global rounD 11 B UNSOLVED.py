s = str(input())
ans = 0
for i in range(1,len(s)):
    if s[i] == s[i-1] == 'W':
        ans+=2
    elif s[i] == 'W' and s[i-1] == 'L':
        ans+=1
    else:
        ans+=0

if s[0] == 'W':
    print(ans+1)
else:
    print(ans)




