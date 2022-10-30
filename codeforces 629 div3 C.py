t = int(input())
while t >0:
    n = int(input())
    s = str(input())
    c = list(s)
    a = []
    b = []
    for i in c:
        if i == '2':
            a.append('1')
            b.append('1')
        elif i == '1':
            a.append('1')
            b.append('0')
        elif i == '0':
            a.append('0')
            b.append('0')

    print(''.join(a))
    print(''.join(b))
    t = t-1