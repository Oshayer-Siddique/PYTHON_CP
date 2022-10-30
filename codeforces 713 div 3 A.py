t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]

    unique_list = []
    for x in arr:
        if x not in unique_list:
            unique_list.append(x)
    

    a = unique_list[0]
    b = unique_list[1]
    a1 = arr.count(a)
    b1 = arr.count(b)
    if a1 == 1:
        p = unique_list[0]
    else:
        p = unique_list[1]

    ans = arr.index(p)

    print(ans+1)
    t = t-1