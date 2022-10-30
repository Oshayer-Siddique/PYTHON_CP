m,n = map(int,input().split())
arr = []

for k in range(m):
    a = list(map(int,input().split()))[:n]
    arr.append(a)
print('\t')
    

mat = [[0 for i in range(m+1)] for j in range(n+1)]

sum1 = 0
for i in range(m):
    mat[i][0] = sum1 + arr[i][0]
    sum1 = mat[i][0]
sum2 = 0
for j in range(n):
    mat[0][j] = sum2 + arr[0][j]
    sum2 = mat[0][j]


sum3 =0
for i in range(1,m,+1):
    for j in range(1,n,+1):
        mat[i][j] = arr[i][j] + min(mat[i-1][j],mat[i][j-1],mat[i-1][j-1])
        sum3 = mat[i][j]


'''for i in range(m):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()
print("\t")

for i in range(m):
    for j in range(n):
        print(mat[i][j],end=" ")
    print()'''
ans = mat[m-1][n-1]

print(ans)