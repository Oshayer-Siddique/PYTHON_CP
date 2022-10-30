print("How to check if two given line segments intersect")

def slope(a,b):
	return (b[1]-a[1])/(b[0]-a[0])

def det(x,y,z):
	return  x[0]*(y[1]*1-(z[1]*1))-x[1]*(y[0]*1-(z[0]*1))+1*(y[0]*z[1]-y[1]*z[0])

A = [10,0]
B = [0,10]
C = [0,0]
D = [10,10]
if slope(A,B) == slope(C,D):
	print("No")
elif ((-1)*(det(C,D,A)/det(C,D,B))) < 0:
	print("No")
else:
	print("yes")


print("inside or outside of a traingle")
def area(x1,y1,x2,y2,x3,y3):
	return abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)//2)
def isinside(x1, y1, x2, y2, x3, y3,x,y):
	A = area (x1, y1, x2, y2, x3, y3)
	A1 = area(x,y,x2,y2,x3,y3)
	A2 = area(x1,y1,x,y,x3,y3)
	A3 = area(x2,y2,x3,y3,x,y)

	if A == A1+ A2+ A3:
		return True
	else:
		return False

if(isinside(0,0,20,0,10,30,10,15)):
	print("yes")
else:
	print("No")
