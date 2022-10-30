'''n = int(input())
res =  (n // 100) + ((n % 100) // 20) + ((n % 20) // 10) + ((n % 10)//5) + ((n % 5)//1)

print(res)'''

'''t = int(input())

while t > 0:
    a,b = map(int,input().split())
    res =  a % b
    print(res)
    t = t-1'''
    
'''a,b,c,d = map(int,input().split())
res = min(b,d) - max(a,c)
if res < 0:
    print(0)
else:
    
    print(res)

n = int(input())
print(25)  '''

t = int(input())
while t > 0:
    n = int(input()) 
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n = int(n/10)

    print(sum)
    t = t-1
    
    