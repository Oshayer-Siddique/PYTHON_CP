n = int(input())
t = [1,2]
for i in range(2,n+1,1):
    res = t[i - 1] + t[i-2]
    t.append(res)

print(t[n-1])
