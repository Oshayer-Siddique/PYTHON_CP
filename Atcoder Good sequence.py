n = int(input())
arr = list(map(int,input().strip().split()))[:n]
arr.sort()
s = set(arr)
a = list(s)
brr = []
flag = 0
#print(a)
for i in range(len(a)):
    brr.append((arr.count(a[i])))
#print(brr)
cnt = 0    
for i in range(len(a)):
    if brr[i] < a[i]:
        cnt += brr[i]
    elif brr[i] > a[i]:
        cnt = cnt + brr[i] - a[i]
        
print(cnt)
