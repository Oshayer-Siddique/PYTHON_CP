# using recursion
#   C(n, k) = C(n-1, k-1) + C(n-1, k)
#   C(n, 0) = C(n, n) = 1
'''def binomial(n,k):
    if k > n:
        return 0
    if k == 0 or k ==  n:
        return 1
    else:
        return binomial(n-1, k-1) + binomial(n-1, k)


n,k = map(int,input().split())

print(binomial(n, k))'''

# using Dynamic Programming
n,k = map(int,input().split())
matrix = [[0 for x in range(k+1)] for x in range(n+1)]

for i in range(n+1):
    for j in range(min(i,k) + 1):
        if j == 0 or j == i:
            matrix[i][j] = 1
        else:
            matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]

ans = matrix[n][k]
print(ans)

for i in range(n+1):
    for j in range(k+1):
        print(matrix[i][j],end=" ")
    print()