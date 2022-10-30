n = int(input())
arr = list(map(int,input().strip().split()))[:n]
ladder = arr[0]
stair = arr[0]
jump = 1
for level  in range(1,len(arr),+1):
    if level == len(arr) - 1:
        ans = jump
    if (level + arr[level] > ladder):
        ladder = level + arr[level]
    stair = stair - 1
    if stair == 0:
        jump = jump+1
        stair = ladder - level
    ans = jump

print(ans)
        
