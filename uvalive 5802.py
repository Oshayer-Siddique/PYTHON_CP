print("FFFRFFFRFFRFFFF")
print("000100010010000")
start_pos = [2,2]
path = [0,0,0,1,0,0,0,1,0,0,1,0,0,0,0]
a = path.count(0)
#print(a)
n = len(path)
def count_0():

	count = 0
	for i in range(n):
		if path[i] == 0:
			count = count+1
		else:
			break
	return count
first_pos = [2,2+count_0()]
print(first_pos)
