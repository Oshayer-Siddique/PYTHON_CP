n = int(input())
b = list(map(int,input().strip().split()))[:n]
m = int(input())
g = list(map(int,input().strip().split()))[:m]
b.sort()
g.sort()
result = 0
arr = []
for i in range(len(b)):
    for j in range(len(g)):
        if abs(b[i] - g[j]) <= 1:
            result+=1
            break
print(result)


