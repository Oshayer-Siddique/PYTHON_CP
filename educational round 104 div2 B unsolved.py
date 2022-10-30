n = 5
matrix = [[0 for i in range(n)] for j in range(n+1)]
arr = [5,4,3,2,1]
stor = [1,2,3,4,5]
for i in range(n+1):
    for j in range(n):
        
        matrix[0][j] = arr[j]
       
for i in range(1,n+1,+1):
    for j in range(n):
        if matrix[i][j] == arr[j]:
            matrix[i][j] = stor[j]+1
        


for i in range(n+1):
    for j in range(n):
        print(matrix[i][j],end=" ")
    
    print()

