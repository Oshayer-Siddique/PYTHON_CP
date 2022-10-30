print("uvalive 6949")
#x1 = int(input("x1 = "))
#y1 = int(input("y1 = "))
def current_pos(path1):
	curX = path1[0]#start position
	r_p_1 =  path1[1]-path1[0]#path distance
	if r_p_1 == 1:
		if t1%2 == 0:
			curX = curX
		else:
			curX = curX+1
	else:
		if t1<= r_p_1:
			curX = curX+t1
		elif t1>r_p_1:
			curX = path1[1]-(t1%r_p_1)
	return curX

path1 = list(map(int,input("path1 = ").strip().split()))[:2]
path2 = list(map(int,input("path2 = ").strip().split()))[:2]
path3 = list(map(int,input("path3 = ").strip().split()))[:2]
path4 = list(map(int,input("path4 = ").strip().split()))[:2]
path5 = list(map(int,input("path5 = ").strip().split()))[:2]
t1 = int(input("t1 = "))
#print(current_pos(path1))
L = []
L.extend([current_pos(path1),current_pos(path2),current_pos(path3),current_pos(path4),
current_pos(path5)])
print(L)
