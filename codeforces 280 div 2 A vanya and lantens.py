#print("diff of 2 elements")

n,l = map(int,input().split())
arr = list(map(int,input().strip().split()))[:n]
arr.sort()
L = []
for i in range(len(arr)-1):
    dif = abs(arr[i]-arr[i+1])
    L.append(dif)


first = float(max(L)/2)

second = arr[0] - 0

third = l - arr[-1]
#print(L)
#print(first)
#print(second)
#print(third)
#print(arr)
res = max(first,second,third)
print(res)
