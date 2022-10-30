
def check(string):
    count = 0
    for i in range(len(string)-6):
        if string[i] == 'a' and string[i+1] == 'b' and string[i+2] == 'a' and string[i+3] == 'c' and string[i+4] == 'a' and string[i+5] == 'b'  and string[i+6] == 'a':
            count += 1
    return count

t = int(input())
while t > 0:
    pat = 'abacaba'
    n = int(input())
    s = str(input())
    flag = 0
    for i in range(0,n-6,+1):
        ss = list(s)
        cur = 1
        for j in range(7):
            if ss[i+j] != '?' and ss[i+j] != pat[j]:
                cur = 0
                break
            else:
                ss[i+j] = pat[j]

        if cur == 1 and check(ss) == 1:
            for k in range(len(s)):
                if ss[k] == '?':
                    ss[k] = 'z'
            
            flag = 1
            print("Yes")
            print(''.join(ss))
    if flag == 0:
        print("No")
    t = t-1


