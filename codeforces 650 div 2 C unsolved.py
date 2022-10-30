s = str(input())
arr = []
def cnt0(s):
    cnt = 0
    for i in s:
        if i == '0':
            cnt += 1
        elif i == '1':
            break
    arr.append(cnt)
    return arr

    
print(cnt0(s))