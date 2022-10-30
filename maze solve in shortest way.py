n,m = map(int,input().split())
start = list(map(int,input().strip().split()))[:2]
end = list(map(int,input().strip().split()))[:2]

arr = []

for k in range(n):
    a = list(map(int,input().split()))[:m]
    arr.append(a)


mat = [[0 for i in range(n)] for j in range(m)]
mat[start[0]][start[1]] = 1

def make_steps(k):
    for i in range(n):
        for j in range(m):
            if mat[i][j] == k:
                if i > 0 and mat[i-1][j] == 0 and arr[i-1][j] == 0:
                    mat[i-1][j] = k+1
                if j > 0 and mat[i][j-1] == 0 and arr[i][j-1] == 0:
                    mat[i][j-1] = k+1
                if i < n-1 and mat[i+1][j] == 0 and arr[i+1][j] == 0:
                    mat[i+1][j] = k+1
                if j < m-1 and mat[i][j+1] == 0 and arr[i][j+1] == 0:
                    mat[i][j+1] = k+1


k = 0
while mat[end[0]][end[1]] == 0:
    k += 1
    make_steps(k)

way = []
i,j = end
k = mat[i][j]
while k > 1:
    if i > 0 and mat[i-1][j] == k-1:
        i,j = i-1,j
        way.append('D')
        k -= 1

    elif j > 0 and mat[i][j-1] == k-1:
        i,j = i,j-1
        way.append('R')
        k -= 1
    elif i < n-1 and mat[i+1][j] == k-1:
        i,j = i+1,j
        way.append('U')
        k -= 1
    elif j < m-1 and mat[i][j+1] == k-1:
        i,j = i,j+1
        way.append('L')
        k -= 1



a = (''.join(way))

final_path = a[::-1]

print(final_path)
