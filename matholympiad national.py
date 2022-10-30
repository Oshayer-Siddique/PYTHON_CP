def sumofint(n):
    sum = 0
    while n != 0:
        sum += (n%10)
        n = int(n/10)
    
    return sum

n = int(input())
for j in range(20):
    if 