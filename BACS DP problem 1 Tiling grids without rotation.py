

def func(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if arr[n] != -1:
        return arr[n]
    else:
        return func(n-1)+func(n-2)

n = int(input())
arr = [-1]*1000
print(func(n))


def fibonacci(n):  
      
    # Taking 1st two fibonacci nubers as 0 and 1  
    f = [0, 1]  
      
      
    for i in range(2, n+1): 
        f.append(f[i-1] + f[i-2]) 
    return f[n] 
n = int(input())    
print(fibonacci()) 