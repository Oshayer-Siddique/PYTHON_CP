t = int(input())
while t > 0:
    n = 100000
    prime = [True for i in range(n+1)] 
    arr = []
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1 
    for p in range(2, n+1): 
        if prime[p]: 
            arr.append(p)

    

    k = []
    k.append(1)
    d = int(input())
    i = 0 
    ans = 1
    cnt = 1
    while(True):
        if cnt == 3:
            break
        if (arr[i] - k[len(k)-1]) >= d:
            k.append(arr[i])
            ans = ans*arr[i]
            cnt = cnt+1
        i = i+1

    print(ans)
    t = t-1
