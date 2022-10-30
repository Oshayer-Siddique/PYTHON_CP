n = int(input())

w = [1,2]
for i in range(2,n+1,+1):
    res = w[i-2] + 2*w[i-1]
    
    w.append(res)
    

print(w[n-1])