print("Fibonacci number DP")
n = int(input())
f = [0,1]
for i in range(2,n+1):
    f.append(f[i-1]+f[i-2])

print(f)
print("Nth fibonacci = ",f[n])

print("Catalan Number DP")
def catalan(n):
    if n == 0:
        return 1
    res = 0
    
    for i in range(n):
        res = res + catalan(i)*catalan(n-i-1)
    
    return res

for i in range(10):
    print(catalan(i),end=" ")



