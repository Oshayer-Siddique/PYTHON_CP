print("UVA live 6802:: Turtle Graphics")


x = int(input("x = "))
y = int(input("y = "))
s = str(input("path = "))
board = [[0]*64 for i in range(64)]
board[x-1][y-1] = 1
dir = 0
curX = x-1
curY = y-1
for c in s:
	if c == 'F':
		if dir == 0:
			curY = curY+1
		elif dir == 1:
			curX = curX-1
		elif dir == 2:
			curY = curY-1
		else:
			curX = curX+1

	else:
		if c == 'L':
			dir = (dir+1)%4
		elif c == 'R':
			dir = (dir+3)%4
print(curX+1)
print(curY+1)
