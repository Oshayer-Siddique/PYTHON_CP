s = input()
p = int(s)
s = s.replace('0',"")
n = int(s)
def checkDivisibility(n, digit) : 

    return (digit != 0 and n % digit == 0) 

def allDigitsDivide(n) : 
    nlist = map(int, set(str(n))) 
    for digit in nlist : 
        if  not (checkDivisibility(n, digit)) : 
            return False
    return True

#print("Yes" if (allDigitsDivide(n)) else "No") 
while(True):
    if allDigitsDivide(p) is True:
        print(p)
        break
    else:
        p = p+1
