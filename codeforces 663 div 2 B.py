I=input
for _ in[0]*int(I()):
    r=0
    for _ in[0]*int(I().split()[0]):s=I();r+=s[-1]=='R'
    print(r+s.count('D'))