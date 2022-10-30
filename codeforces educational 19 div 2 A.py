import math
n , k = map(int,input().split())
arr = []
stor = []
for i in range(2,int(math.sqrt(n))+1,+1):
    while n % i == 0:
        n = n//i
        arr.append(i)
if n >= 2:
    arr.append(n)
if k > len(arr):
    print(-1)
else:
    for j in range(k-1):
        print(arr[j],end=" ")
    product = 1
    for u in range(k-1,len(arr)):
        product = product*arr[u]

    print(product)

