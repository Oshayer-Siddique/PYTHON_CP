def catalan(n):
    if n == 0:
        return 1
    res = 0
    for i in range(n):
        res = res + catalan(i) * catalan(n-i-1)
    return res

n = int(input())

for i in range(n):
    print(catalan(i),end=" ")

#using Dynamic
n = int(input())
cat = [0]*(n+1)

cat[0] = 1
cat[1] = 1

for i in range(2,n+1,+1):
    for j in range(i):
        cat[i] += cat[j] * cat[i - j -  1]

print(*cat,sep=" ")