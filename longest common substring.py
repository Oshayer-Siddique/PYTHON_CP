M = str(input())
N = str(input())
m = len(M)
n = len(N)
matrix = [[0 for u in range(n+1)] for v in range(m+1)]
result = 0
for i in range(m+1):
    for j in range(n+1):
        if (i == 0 or j == 0):
            matrix[i][j] = 0
        elif M[i-1] == N[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
            result = max(result,matrix[i][j])
        else:
            matrix[i][j] = 0

        print(matrix[i][j],end=" ")

        

    print()

print(result)