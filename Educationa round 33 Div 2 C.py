# cook your dish here
import sys
from collections import defaultdict
from collections import deque
sys.setrecursionlimit(10**6)
n,m=list(map(int,input().split()))
c=list(map(int,input().split()))
d=defaultdict(list)
for i in range(m):
    x,y=map(int,input().split())
    d[x].append(y)
    d[y].append(x)
ans=0
visited=[0]*(n+1)
for i in range(1,n+1):
    if visited[i]==0:
        q=deque()
        q.append(i)
        m=10**(9)
        visited[i]=1
        while len(q):
            x=q.popleft()
            m=min(m,c[x-1])
            for j in d[x]:
                if visited[j]==0:
                    visited[j]=1
                    q.append(j)
        ans=ans+m
print(ans)
