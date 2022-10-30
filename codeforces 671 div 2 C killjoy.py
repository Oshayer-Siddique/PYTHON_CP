import math

#print("codeforces 671 div 2 C")
def find(x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

#print(arr)
def ckeckList(arr):
    ele = arr[0]
    chk = True
    for item in arr:
        if ele != item:
            chk = False
            break;
    if (chk == True):
        print(0)
    else:
        sum1 = 0
        for j in range(find(x)):
            sum1 = sum1 + abs(arr[j])

        t1  = abs(x-(sum1))
        #print((t1))

        sum2 = 0
        for k in range(find(x)+1,len(arr)):
            sum2 = sum2 + abs(arr[k])

        t2 = abs(x - (sum2))
        #print((t2))
        if t1 == t2:
            print(1)
        else:
            print(2)

t = int(input())
for testcase in range(t):
    n,x = map(int,input().split())
    arr = list(map(int,input().strip().split()))[:n]
    arr.append(x)
    arr.sort()
    ckeckList(arr)
