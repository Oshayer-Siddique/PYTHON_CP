t = int(input())
while t > 0:
    n,k = map(int,input().split())
    s = str(input())
    arr = list(s)
    for i in range(n):
        if arr[i] == '*':
            arr[i] ='x'
            break   
    for i in range(n-1,-1,-1):
        if arr[i] == '*':
            arr[i] = 'x'
            break



    stor = []
    for i in range(n):
        if arr[i] == 'x':
            stor.append(i)
    c = len(stor)
    if c == 1:
        ans = 1
    else:
        dis = stor[1] - stor[0]-1

        a = 2*(k-1)
    #print("a = ",a)

        put = dis//a
        ans = put + 2

    print("ans = ",ans)
    t = t-1
#print("dis=",dis)
#print(''.join(arr))