t = int(input())
while t > 0:
    s = str(input())
    arr = list(s)

    def check(s,arr):
        
        stor = []
        for i in range(len(arr)-1,-1,-1):
            stor.append(arr[i])
        if arr == stor:
            return True
        else:
            return False
    arr.append('a')
    if check(s,arr) == False:
        print("YES")
        print(*arr,sep="")
    elif check(s,arr) == True:
        del(arr[-1])
        arr.insert(0,'a')
        if check(s,arr) == False:
            print("YES")
            print(*arr,sep="")
        else:
            print("NO")
    t = t-1