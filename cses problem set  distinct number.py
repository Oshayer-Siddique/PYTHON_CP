n = int(input())
arr = list(map(int,input().strip().split()))[:n]
unilist = []
for x in arr:
    if x not in unilist:
        unilist.append(x)


ans = len(unilist)

print(ans)