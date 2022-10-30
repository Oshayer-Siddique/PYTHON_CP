t = int(input())
while(t>0):
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    max_product = arr[0]*arr[1]*arr[2]*arr[3]*arr[4]
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    for m in range(l+1,n):
                        if arr[i]*arr[j]*arr[k]*arr[l]*arr[m] > max_product:
                            max_product = arr[i] * arr[j] * arr[k] * arr[l] * arr[m]

    print(max_product)
    t = t-1