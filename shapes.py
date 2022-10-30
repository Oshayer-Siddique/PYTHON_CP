
print("triangle")
n = int(input("n = "))
for i in range(n+1):
	for j in range(i):
		print("#",end = "")

	print()

print("Hollow triangle")
n = int(input("n  = "))
for row in range(n):
	for coloumn in range(n):
		if coloumn == 0 or coloumn == row or row == (n-1):
			print("$",end = "")
		else:
			print(end = " ")
	print()

print("Hollow triangle 1")
n = int(input("n = "))
for row in range(n):
	for column in range(n):
		if column == n-1 or row == 0 or row == column:
			print("*",end = "")
		else:
			print(end=" ")

	print()

print("diamond")
n = 10
for i in range(n+1):
	for j in range(n-i):
		print(" ",end="")
	for k in range(i):
		print(" *",end="")
	print()
for l in range(n):
	for m in range(l):
		print(" ",end="")
	for p in range(n-l):
		print("* ",end="")

	print()
