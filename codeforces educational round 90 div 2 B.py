t = int(input())
while t > 0:
    s = str(input())
    if (min(s.count('0'),s.count('1'))) % 2 == 1:
        print("DA")
    else:
        print("NET")
    t = t-1        
