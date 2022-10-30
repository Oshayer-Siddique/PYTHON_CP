n = int(input())
a,b,c = map(int,input().split())
arr = list(map(int,input().strip().split()))[:n]
s = str(input())
ss = list(s)
arr1 = []
for i in range(5):
    a = list(map(int,input().split()))[:5]
    arr1.append(a)



for i in range(5):
    for j in range(5):
        print(arr1[i][j],end=" ")
    print()
##How to find the index of the nth time an item appears in a list?
from itertools import islice



def nth_index(iterable, value, n):
    matches = (idx for idx, val in enumerate(iterable) if val == value)
    return next(islice(matches, n-1, n), None)

x = 'wessszzs'
idx = nth_index(x, 's', 4)
print(idx)