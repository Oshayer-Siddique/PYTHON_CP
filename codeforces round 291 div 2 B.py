n, x_0,y_0 = map(int,input().split())
arr = []
 
for i in range(n):
    a = list(map(int,input().split()))[:2]
    arr.append(a)
 
def tangent(x_0,y_0,p1,p2):
    return float((y_0-p2)/(x_0-p1))
arr1 = []
for i in range(n):
    if arr[i][0] == x_0:
        arr1.append(-0.0000001)
        continue
    for j in range(2):
        
        a = tangent(x_0,y_0,arr[i][0],arr[i][1])
    arr1.append(a)
#print(arr1)
 
arr2 = []
for k in arr1:
    if k not in arr2:
        arr2.append(k)
if -0.0000001 in arr2:
    print(len(arr2))
else:
    print(len(arr2))