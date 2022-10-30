n = int(input())
arr = []
for k in range(n):
  a = list(map(str,input().split()))[:n]
  arr.append(a)

paths = [[0 for i in range(n)] for j in range(n)]
if arr[0][0] == '.':
  paths[0][0] = 1

for i in range(1,n):
  if arr[i][0] == '.':
    paths[i][0] = 1
  else:
    paths[i][0] = 0


for j in range(1,n):
  if arr[0][j] == '.':
    paths[0][j] = 1
  else:
    paths[0][j] = 0

    
for i in range(1,n):
  for j in range(1,n):
    if arr[i][j] == '.':
      paths[i][j] = paths[i-1][j] + paths[i][j-1]

ans = paths[n-1][n-1]

'''for  i in range(n):
  for j in range(n):
    print(paths[i][j],end=" ")
  
  print()'''


print(ans)