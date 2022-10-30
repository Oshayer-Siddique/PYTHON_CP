n = int(input())
arr = list(map(int,input().strip().split()))[:n]

hashmap = {}

out = []
sum1  =0

for i in range(n):
    sum1 += arr[i]
    if sum1 == 0:
        out.append((0,i))
        

    al = []
    if sum1 in hashmap:
        al = hashmap.get(sum1)
        for j in range(len(al)):
            out.append((al[j]+1,i))
            
            
    al.append(i)
    hashmap[sum1] = al
    

    
print(len(out))