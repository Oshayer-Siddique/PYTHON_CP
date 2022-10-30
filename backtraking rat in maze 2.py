ans = [
[0]*5,
[0]*5,
[0]*5,
[0]*5,
[0]*5
]
#ans=[[0]*5]*5
def isSafe(arr, i, j, n):
	if i<n and j<n and arr[i][j]==1:
		return True
	return False

def func(arr, i, j, n):
	if i==n-1 and j==n-1:
		ans[i][j]=1
		return True
	#print(ans)
	if isSafe(arr, i, j, n) == True:
		ans[i][j] = 1
		if func(arr, i, j+1, n) == True:
			return True
		if func(arr, i+1, j, n) == True:
			return True
		ans[i][j] = 0
		return False
	return False
arr=[
	[1, 0, 1, 0, 1],
	[1, 1, 1, 1, 1], 
	[0, 1, 0, 1, 0],
	[1, 0, 0, 1, 1],
	[1, 1, 1, 0, 1]
]
func(arr, 0, 0, 5)
for i in range(5):
	print(ans[i])


