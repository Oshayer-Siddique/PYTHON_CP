n,m = map(int,input().split())
arr = []
lit = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    a = list(map(int,input().split()))[:m]
    arr.append(a)

lit = [[0 for i in range(m)] for j in range(n)]

for  i in range(n):
    for j in range(m):
        lit[i][j] = arr[i][j]


def checkprime(x):
    flag = False
    if x > 1:
        for i in range(2,(x//2) + 1,+1):
            if x % i == 0:
                flag = True

                break
    if flag == True:
        return -1
    elif x == 1:
        return -1
    else:
        return 1
#x = int(input())
#print(checkprime(x))

stor = [[0 for i in range(m)] for j in range(n)]

#print(stor)

for i in range(n):
    for j in range(m):
        if checkprime(arr[i][j]) == 1:
            stor[i][j] = arr[i][j]
        else:
            for u in range(10000):
                if checkprime(arr[i][j]) == -1:
                    arr[i][j] += 1
                elif checkprime(arr[i][j]) == 1:
                    stor[i][j] = arr[i][j]
                    break
            
#print("\t")
#for i in range(n):
    #for j in range(m):
        #print(stor[i][j],end=" ")
    
    #print()
#print("\t")

finals = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        finals[i][j] = stor[i][j] - lit[i][j]
        #print(finals[i][j],end=" ")
    
    #print()

    
sum1 = 0
mini1 = []
for i in range(n):
    for j in range(m):
        sum1 +=  finals[i][j]
    mini1.append(sum1)
    sum1 = 0

m1 = min(mini1)

sum2 = 0
mini2 = []
for i in range(m):
    for j in range(n):
        sum2 += finals[j][i]
    mini2.append(sum2)
    sum2 = 0

m2 = min(mini2)

ans = min(m1,m2)
print(ans)

