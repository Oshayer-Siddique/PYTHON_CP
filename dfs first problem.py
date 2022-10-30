from collections import defaultdict

def vec():
    return set()

n ,m = map(int,input().split())

d = defaultdict(vec)
for t in range(m):
    u,v = map(int,input().split())
    d[u].add(v)
    d[v].add(u)

def dfs(i):
    vec[i] = 1
    for j in d[i]:
        if vec[j] == 0:
            dfs(j)

c = 0
vec = [0]*(n+1)
for i in range(1,n+1,+1):
    if vec[i] == 0:
        dfs(i)
        c+=1

print(c)