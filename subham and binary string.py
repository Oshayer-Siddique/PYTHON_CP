
#print("left rotation")
t = int(input())
while t > 0:
 
    def leftrotate(arr):
        s = arr[1:] + arr[0]
        return s
 
    x = int(input())
    arr = str(input())
    s = str
    #print(leftrotate(arr))
    L = []
    L1 = []
    L.append((leftrotate(arr)))
    for i in range(len(arr) - 1):
     
        cur = leftrotate(arr)
        arr = cur
 
    #print(leftrotate(arr))
        L.append((leftrotate(arr)))
 
#print(L)
#print(type(L[0]))
 
    def binarytodecimal(n):
      return int(n,2)
 
 
 
    for i in L:
      if binarytodecimal(i) % 2 == 0:
        L1.append(binarytodecimal(i))
  
    print(len(L1))
    t = t-1