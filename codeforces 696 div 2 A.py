t = int(input())
while t > 0:
    n = int(input())
    s = str(input())
    arr = []
    ss = list(s)
    arr.append('1')
    for i in range(1,n,+1):
        if ss[i] == '1':
            if ss[i-1] == '1' and arr[i-1] == '1':
                arr.append('0')
            elif ss[i-1] == '1' and arr[i-1] == '0':
                arr.append('1')
            elif ss[i-1] == '0' and arr[i-1] == '1':
                arr.append('1')
            elif ss[i-1] == '0' and arr[i-1] == '0':
                arr.append('1')
        elif ss[i] == '0':
            if ss[i-1] == '1' and arr[i-1] == '1':
                arr.append('1')
            elif ss[i-1] == '1' and arr[i-1] == '0':
                arr.append('0')
            elif ss[i-1] == '0' and arr[i-1] == '1':
                arr.append('0')
            elif ss[i-1] == '0' and arr[i-1] == '0':
                arr.append('1')


    print(''.join(arr))
    t = t-1