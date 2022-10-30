def repeater(s1):
    i = (s1+s1)[1:-1].find(s1)
    if i == -1:
        return s1
    else:
        return s1[:i+1]
def lcm(x1, y1):
   if x1 > y1:
       greater = x1
   else:
       greater = y1

   while(True):
       if((greater % x1 == 0) and (greater % y1 == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
t1=int(input(""))
while(t1!=0):
    s= input("")
    y=input("")
    if(repeater(s) == repeater(y)):
        for i in range(lcm(len(s),len(y))//len(repeater(s))):
            print(repeater(s),end='')
       
    else:
        print(-1)

    print('\t')
    t1=t1-1
