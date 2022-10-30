t = int(input())
while t >0:
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    stor = []
    for i in range(len(arr)):
        for j in range(i):
            ans = abs(arr[i]-arr[j])
            stor.append(ans)
    #print(stor)

    output = []
    for x in stor:
        if x not in output:
            output.append(x)
    ans = len(output)
    print(ans)
    t = t-1