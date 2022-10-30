n = int(input())
arr = list(map(int,input().strip().split()))[:n]
def function(n,k):
    for i in range(n-k+1):
        current_sum = 0
        for j in range(k):
            current_sum += arr[i+j]
        if current_sum == 0:
            return 1
            break
stor = []    
for k in range(1,n+1,+1):
    ans = function(n, k)
    stor.append(ans)
flag = 0
for i in range(len(stor)):
    if stor[i] == 1:
        flag = 1
if flag ==1 :
    print("YES")
else:
    print("NO")