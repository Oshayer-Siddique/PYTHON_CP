t,x1,y1,x2,y2  = map(int,input().split())
s = str(input())
a = x2 - x1
b = y2 - y1
from itertools import islice

def nth_index(iterable, value, n):
    matches = (idx for idx, val in enumerate(iterable) if val == value)
    return next(islice(matches, n-1, n), None)
if a > 0 and b > 0:
    f = nth_index(s,'E',a)
    l = nth_index(s,'N',b)
    if s.count('E') < abs(a) or s.count('N') < abs(b):
        final = -1
    else:
        final = max(f,l)+1
elif a > 0 and b < 0 :
    f = nth_index(s,'E',abs(a))
    l = nth_index(s,'S',abs(b))
    if s.count('E') < abs(a) or s.count('S') < abs(b):
        final = -1
    else:
        final = max(f,l)+1
elif a < 0 and b > 0:
    f = nth_index(s,'W',abs(a))
    l = nth_index(s,'N',abs(b))
    if s.count('W') < abs(a) or s.count('N') < abs(b):
        final = -1
    else:
        final = max(f,l)+1
elif a < 0 and b < 0:
    f = nth_index(s,'W',abs(a))
    l = nth_index(s,'S',abs(b))
    if s.count('W') < abs(a) or s.count('S') < abs(b):
        final = -1
    else:
        final = max(f,l)+1
elif a > 0 and b == 0:
    f = nth_index(s,'E',abs(a))
    if s.count('E') < abs (a):
        final = -1
    else:
        final = f+1

elif a < 0 and b == 0:
    f = nth_index(s,'W',abs(a))
    if s.count('W') < abs (a):
        final = -1
    else:
        final = f+1
elif a == 0 and b > 0:
    f = nth_index(s,'N',abs(b))
    if s.count('N') < abs (b):
        final = -1
    else:
        final = f+1
elif a == 0 and b < 0:
    f = nth_index(s,'S',abs(b))
    if s.count('S') < abs (b):
        final = -1
    else:
        final = f+1
print(final)




