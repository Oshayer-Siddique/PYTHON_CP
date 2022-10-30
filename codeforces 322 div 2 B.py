
'''n,sum = map(int,input().split())
arr = []
def func(n):
    return n*(n+1)//2
i = 1
while (func(i)<sum):
    arr.append(func(i))
    i = i+1
print(arr)
a = i-1
print(a)

res = 0
a,b = map(float,input().split())
if a % 5 == 0 and a < b:
    res = (b-a - 0.5)
else:
    res = (b)
    
print("{:.2f}".format(res))

n , k = map(int,input().split())

for i in range(1,k+1,+1):
    if n % 10 != 0:
        n = n - 1
    else:
        n = n //10
        
print(n)   

a,b,c = map(int,input().split())
arr = []
arr.append(a)
arr.append(b)
arr.append(c)
arr.sort()
if arr[0] + arr[1] > arr[2]:
    print(0)
else:
    print(arr[2] -(arr[0] + arr[1]) +1)
    
    
n,a,x,y = map(int,input().split())
if n < a:
    res = 0
else:
    res = a*x + (n-a)*y
print(res)

n,k = map(int,input().split())
cnt = 0
for i in range(n):
    i = int(input())
    if i % k == 0:
        cnt += 1
        

print(cnt)

n,a,x,y = map(int,input().split())
if n > a:
    res = a*x + (n-a)*y
else:
    res = n * x
print(res)'''








n,m = map(int,input().split())
flag = True
while flag:
    for i in range(1,n+1,+1):
        if m >= i:
            m = m - i
        else:
            flag = False
            break

print(m)

