def func(A,n,k,ch):
    i = 0
    j = 0
    cnt = 0
    maxlen = 1
    while i < n:
        if A[i] != ch:
            cnt += 1
        while cnt > k:
            if A[j] != ch:
                cnt -= 1
            j += 1
        maxlen = max(maxlen,i-j+1)
        i = i+1
    return maxlen


n,k = map(int,input().split())
A = str(input())

m1 = func(A,n,k,'a')
m2 = func(A,n,k,'b')
ans = max(m1,m2)
print(ans)