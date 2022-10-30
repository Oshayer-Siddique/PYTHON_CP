n = int(input())
arr= []
for i in range(1,n+1,+1):
    arr.append(i*2)
    arr.append(i*3)
    arr.append(i*5)


arr.insert(0, 1)
arr.sort()
#print(arr)

new = set(arr)
#print(new)

last = list(new)
last.sort()
print(last)
ans = last[n-1]

print(ans)