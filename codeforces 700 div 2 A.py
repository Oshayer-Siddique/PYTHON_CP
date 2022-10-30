t = int(input())
while t > 0:
    s = str(input())
    arr = []
    for i in range(len(s)):
        if i % 2 == 0 and s[i] != 'a':
            arr.append('a')
        elif i % 2 == 0 and s[i] == 'a':
            arr.append('b')
        elif i % 2 == 1 and s[i] != 'z':
            arr.append('z')
        elif i % 2 == 1 and s[i] == 'z':
            arr.append('y')
        
    

    print(''.join(arr))
    t = t-1