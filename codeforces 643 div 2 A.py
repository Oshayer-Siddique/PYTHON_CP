

#print("codeforces 643 div 2 A")

def function(n,k):
    for i in range(1,k,+1):
        temp = n
        max_v = 0
        min_v = 9
        while(n>0):
            r = n % 10
            max_v = max(r,max_v)
            min_v = min(r,min_v)
            n = n//10

        n = temp + max_v * min_v
        if min_v == 0:
            break
    print(n)
t = int(input())
for testcase in range(t):
    n,k = map(int,input().split())

    (function(n,k))
