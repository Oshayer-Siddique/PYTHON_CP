def repeater(s1):
    i = (s1+s1)[1:-1].find(s1)
    if i == -1:
        return s1
    else:
        return s1[:i+1]

s = str(input())
print(repeater(s))