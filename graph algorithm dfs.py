adj =  [[0 for i in range(100)] for j in range(100)]
color = [0 for i in range(100)]
white = 1
gray = 2
black = 3
node,edge = map(int,input().split())
def dfsvisit(x):
    color[x] = gray
    for i in range(node):
        if adj[x][i] == 1:
            if color[i] == white:
                dfsvisit(i)

def dfs():
    for i in range(node):
        color[i] = white
    for i in range(node):
        if color[i] == white:
            dfsvisit(i)





for i in range(edge):
    n1,n2 = map(int,input().split())
    adj[n1][n2] = 1
    adj[n2][n1] = 1

dfs()