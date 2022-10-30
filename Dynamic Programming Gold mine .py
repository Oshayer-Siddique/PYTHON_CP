n,m = map(int,input().split())
arr = []
stor = []

for k in range(n):
  a = list(map(int,input().split()))[:m]
  arr.append(a)

mat = [[0 for i in range(n)] for j in range(m)]

for col in range(n-1,-1,-1):
    for row in range(m):
        if col == n-1:
            right = 0
        else:
            right = mat[row][col+1]
        if row == 0 or col == n-1:
            right_up = 0
        else:
            right_up = mat[row-1][col+1]
        if row == m-1 or col == n-1:
            right_down = 0
        else:
            right_down = mat[row+1][col+1]
        mat[row][col] = arr[row][col] + max(right,right_up,right_down)
stor = []
for x in range(m):
    stor.append(mat[x][0])

ans = max(stor)
    
'''for i in range(n):
  for j in range(m):
    print(mat[i][j],end=' ')
  print()'''


print(ans)