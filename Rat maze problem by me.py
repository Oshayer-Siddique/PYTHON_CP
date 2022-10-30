N = 6
maze = []
for k in range(N):
    a = list(map(str,input().split()))[:N]
    maze.append(a)

def issafe(maze,x,y):
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True
    else:
        return False

def solveuntil(maze,x,y,sol):
    if x == N-1 and y == N-1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True
    if issafe(maze,x,y) == True:
        if sol[x][y] == 1:
            return False
        else:
            sol[x][y] = 1
        if solveuntil(maze,x+1,y,sol) == True:
            return True
        if solveuntil(maze,x-1,y,sol) == True:
            return True
        if solveuntil(maze,x,y+1,sol) == True:
            return True
        if solveuntil(maze,x,y-1,sol) == True:
            return True
        else:
            sol[x][y] = 0
            return False
def solve(maze):
    sol = [[0 for j in range(N)] for i in range(N)]
    if solveuntil(maze,0,0,sol) == False:
        print("NO WAY")
        return False
    else:
        printsolve(sol)
        return True
def printsolve(sol):
    for i in sol:
        for j in i:
            print(str(j) + " ",end = "")
        print("")


solve(maze)