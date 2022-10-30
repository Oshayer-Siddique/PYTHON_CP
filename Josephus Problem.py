n,k = map(int,input().split())

def function(n,k):
    if n == 1:
        return 1
    else:
        return (function(n-1, k) + k - 1) % n + 1


print(function(n, k)) 
    


'''Josephus problem sequence '''

n = int(input())
children = [0] * n

for i in range(n):
    children[i] = i + 1

while len(children) > 1:
    survivor = []
    for i in range(0,len(children),1):
        if i % 2 == 1:
            print(children[i],end=" ")
        else:
            survivor.append(children[i])
    
    if len(children) % 2 == 0:
        children = survivor
    else:
        starter = survivor[-1]
        survivor.pop()
        children.clear()
        children.append(starter)
        for z in survivor:
            children.append(z)

print(children[0])
    
