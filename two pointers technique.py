#Given a sorted array A (sorted in ascending order), having N integers,
# find if there exists any pair of elements (A[i], A[j]) 
# such that their sum is equal to X
n,s = map(int,input().split())
arr = list(map(int,input().strip().split()))[:n]
i , j, flag = 0 , n-1 , 0
while i < j:
    if arr[i] + arr[j] == s:
        flag = 1
        break
    elif arr[i] + arr[j] < s:
        i = i+1
    else:
        j = j-1

if flag == 1:
    print("YES",i+1,j+1)
else:
    print("NO")
