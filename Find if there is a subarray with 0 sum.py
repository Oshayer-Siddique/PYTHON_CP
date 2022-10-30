n = int(input())
arr = list(map(int,input().strip().split()))[:n]

presum = [0 for i in range(n)]
presum[0] = arr[0]



for i in range(1,n):
    presum[i] += presum[i-1]+ arr[i]

s = len(set(presum))

#print(s)
#print(n)
if s == n:
    print("No")
else:
    print("Yes")

#print(presum)