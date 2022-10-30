s = str(input())
cnt = 0
stor = []
i = 0
while i < len(s):
    if s[i] == '0':
        cnt+=1
    
    if s[i] == '1':
        cnt = 0

    i+=1
    stor.append(cnt)

#print(stor)
n = len(stor)
final = []

for i in range(len(stor)-1):
    if stor[i+1] == 0:
        final.append(stor[i])

if stor[-1] != 0:
    final.append(stor[-1])  

ans = max(final)
print(final)
print(ans)





