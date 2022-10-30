
def func(n):
    tot = 0
    while (n > 0):
        dig = n%10
        tot = tot+dig
        n = n//10
    return tot

#print(func(n))
arr = []
for i in range(1,445,+1):
    arr.append(func(i))

print(arr)

ans = sum(arr)

print(ans)
