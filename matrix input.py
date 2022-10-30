n,m = map(int,input().split())
arr = []
first = []
second = []
for k in range(n):
  a = list(map(int,input().split()))[:m]
  arr.append(a)
  
for i in range(n):
  for j in range(m):
    if arr[i][j] == 1:
      x = i+1
      y = j+1
  for j in range(2):
    print(x,y)
  
  
      

      
      
      


'''for i in range(n):
  for j in range(m):
    print(arr[i][j],end=' ')
  print()'''
