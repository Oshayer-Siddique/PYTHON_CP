a = str(input())
b = str(input())

 
chance = 0
def factorial(n):
    fact = 1
    for i in range(1,n+1,+1):
        fact = fact * i
    return fact
 
 
def combination(x,y):
    return factorial(x)//(factorial(x-y)*factorial(y))
 
 
des = 0
curpos = 0
unrec = 0
for i in a:
    if i == '+':
        des+=1
    elif i == '-':
        des -= 1
for i in b:
    if i == '+':
        curpos+=1
    elif i == '-':
        curpos -= 1
    elif i == '?':
        unrec += 1
 
run = des - curpos
if run >= 0:
    plus = (unrec + run)/2
    
    if round(plus) == plus:
        chance = combination(unrec,round(plus))
    else:
        chance = 0
elif run < 0:
    minus = (unrec + abs(run))/2
    if round(minus) == minus:
        chance = combination(unrec,round(minus))
    else:
        chance = 0
  
 
#print(chance)
prob =  chance/(2**(unrec))  
 
 
if abs(des - curpos) == 2 and unrec == 0:
    print(0.0000000000)
else:
    print(prob)