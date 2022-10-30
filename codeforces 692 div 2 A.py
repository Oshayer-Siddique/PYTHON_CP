t = int(input())
while t > 0:
    n = int(input())
    s = input()
    count = 0
    for i in range(len(s)-1,-1,-1):
        if s[i] == ')':
            count+=1
        else:
            break
    print(count)
    res = n - count
    if count > res:
        print("YES")
    else:
        print("NO")
    t = t-1
