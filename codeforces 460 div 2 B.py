k = int(input())
#n = int(input())
def sumofint(n):
    sum = 0
    while n != 0:
        sum += (n%10)
        n = int(n/10)
    
    return sum
arr = []
for n  in range(10000000):
    if sumofint(n) == 10:
        arr.append(n)

#print(arr)
ans = arr[k-1]
print(ans)