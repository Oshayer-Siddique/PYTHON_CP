n = int(input())
table = [0 for k in range(n)]
coin = [1,2]
k = len(coin)

table[0] = 1
for i in range(1,n+1,+1):
    for j in range(1,k+1,+1):
        if i >= coin[j]:
            table[i] += table[i - coin[j]]

print(table[n-1])