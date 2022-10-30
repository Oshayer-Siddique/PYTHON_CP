t = int(input())
while t > 0:
    s = str(input())
    flag = 0
    arr = list(s)
    if arr[0] == 'A':
        for i in range(len(arr)):
            if arr[i] == 'A':
                arr[i] = '('
    elif arr[0] == 'B':
        for i in range(len(arr)):
            if arr[i] == 'B':
                arr[i] = '('
    elif arr[0] == 'C':
        for i in range(len(arr)):
            if arr[i] == 'C':
                arr[i] = '('
    if arr[-1] == 'A':
        for i in range(len(arr)):
            if arr[i] == 'A':
                arr[i] = ')'
    elif arr[-1] == 'B':
        for i in range(len(arr)):
            if arr[i] == 'B':
                arr[i] = ')'
    elif arr[-1] == 'C':
        for i in range(len(arr)):
            if arr[i] == 'C':
                arr[i] = ')'
    #print(''.join(arr))
    first_b = arr.count('(')
    last_b = arr.count(')')
    if first_b > last_b:
        for i in range(len(arr)):
            if arr[i] == 'A' or arr[i] == 'B' or arr[i] == 'C':
                arr[i] = ')'
    elif last_b > first_b:
        for i in range(len(arr)):
            if arr[i] == 'A' or arr[i] == 'B' or arr[i] == 'C':
                arr[i] = '('
    elif first_b == last_b and ((arr.count('(') + arr.count(')')) < len(arr)) :
        flag = 1
    
    if arr[0] == ')' or arr[-1] == '(':
        print("NO")
    elif flag == 1:
        print("NO")
    elif arr.count('(') == arr.count(')'):
        print("YES")
    
    else:
        print("NO")
    #print(''.join(arr))
    t = t-1
    


    