t = int(input())
while t > 0:

    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    arr.sort()
    if n == 1:
        print(arr[0])
    else:
        sum_arr = [0 for i in range(n+1)]
        sum_arr[0] = arr[0]
        for i in range(1,n):
            sum_arr[i] = sum_arr[i-1] + arr[i]
    #print(sum_arr[i])


#print(sum_arr)

        ans = sum(sum_arr) - sum_arr[0]
        print(ans)
    t = t-1

