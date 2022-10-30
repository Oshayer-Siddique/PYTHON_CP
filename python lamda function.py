x = lambda a : a + 10

print(x(5))

x = lambda a,b  : a * b
print(x(5,6))
n = int(input())
vec  = [[int(i) for i in input().split()] for j in range(n)]
print(vec)
vec.sort(key = lambda x : x[0])
