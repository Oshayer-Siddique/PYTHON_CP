'''cnt = 0
for i in range(1,2036,+1):
    if 2036 % i == 12:
        cnt+=1
        #print(i)

print(cnt)'''

for i in range(1,210):
    if 144 % i == 0 and 196 % i == 0:
        print(i)
print('\t')
for i in range(1,210):
    if 196 % i == 0 and 210 % i == 0:
        print(i)
print('\t')
for i in range(1,210):
    if 144 % i == 0 and 210 % i == 0:
        print(i)