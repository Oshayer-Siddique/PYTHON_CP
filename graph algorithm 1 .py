adj =  [[0 for i in range(100)] for j in range(100)]
#node,edge = map(int,input().split())
x  =  int(input())
stor = []
node,edge = map(int,input().split())
for i in range(edge):
    n1,n2 = map(int,input().split())
    adj[n1][n2] = 1
    adj[n2][n1] = 1

for i in range(node):
    if adj[x][i] == 1:
        stor.append(i)

print(*stor,sep=" ")
print("\n")

'''
5 6
0 1
2 0 
2 1
1 3
3 4
1 4'''


for i in range(node):
    for j in range(node):
        print(adj[i][j],end=" ")
    
    print()


