arr = list(map(int,input().strip().split()))[:3]
sum = 0
for i in range(1,len(arr)+1,+1):
    for j in range(i,len(arr)+1,+1):
        sum = sum+((arr[j-1])/j)

print(round(sum))

