print("codeforces Amr and pins B 1400")
import math
r,x1,y1,x2,y2 = map(int,input().split())
d = math.sqrt((x2-x1)**2+(y2-y1)**2)
res = math.ceil(d/(2*r))
print(res)
