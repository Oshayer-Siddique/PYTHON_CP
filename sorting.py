print("selection sort")
def selection_sort(arr):
	for i in range(len(arr)):
		index = i
		for j in range(i+1,len(arr)):
			if arr[j]<arr[index]:
				index = j
		if index != i:
			arr[i],arr[index] = arr[index],arr[i]
	return arr
arr = [1,4,3,6,4,4,44,77,-100,656]
print(selection_sort(arr))

print("Bubble sort")

def bubble_sort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-i-1):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
	return arr

arr = [1,4,3,5,7,3,2,6,-199]
print(bubble_sort(arr))

print("insertion sort")

def insertion_sort(arr):
	for i in range(1,len(arr)):
		key = arr[i]
		j = i-1
		while j>=0 and key < arr[j]:
			arr[j+1] = arr[j]
			j = j-1
			arr[j+1] = key

	return arr

arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))

print("Count all distinct pairs with difference equal to k")
arr = [8, 12, 16, 4, 0, 20]
k = int(input("k = "))

count = 0
for i in range(len(arr)):
	for j in range(i+1,len(arr)):
		if abs(arr[i]-arr[j]) == k:
			count = count+1

print(count)

print("Maximum product of a triplet (subsequence of size 3) in array")
n = int(input("n = "))
arr = list(map(int,input("List = ").strip().split()))[:n]
max_product = arr[0]*arr[1]*arr[2]
for i in range(len(arr)):
	for j in range(i+1,len(arr)):
		for k in range(j+1,len(arr)):
			if arr[i]*arr[j]*arr[k]>=max_product:
				max_product = arr[i]*arr[j]*arr[k]

print(max_product)

print("Find missing elements of a range")
n = int(input("n = "))
arr = list(map(int,input("List = ").strip().split()))[:n]
low = int(input("Low = "))
high = int(input("High = "))
L = []
for i in range(low,high):
	if i not in arr:
		L.append(i)

L.sort()
print(L)

print("Find the point where maximum intervals overlap")
arr = [1, 2, 9, 5, 5]
exit = [4, 5, 12, 9, 12]
arr.sort()
exit.sort()
guest_in = 1
max_guest = 1
i = 1
j = 0
time = arr[0]
n = len(arr)
while(i<n and j<n):
	if arr[i]<=exit[j]:
		guest_in = guest_in+1
		if guest_in>max_guest:
			max_guest = guest_in
			time = arr[i]
		i = i+1
	else:
		guest_in = guest_in-1
		j = j+1

print("max guest = ",max_guest,"\n","time = ",time)

print("Find minimum difference between any two elements")
arr = [1, 5, 3, 19, 18, 25]
min_diff = abs(arr[0]-arr[1])
for i in range(len(arr)):
	for j in range(i+1,len(arr)):
		if abs(arr[i]-arr[j])<min_diff:
			min_diff = abs(arr[i]-arr[j])

print(min_diff)

print("Minimum sum of two numbers formed from digits of an array")
arr = [6, 8, 4, 5, 2, 3]
#Input: [6, 8, 4, 5, 2, 3]
#Output: 604
#The minimum sum is formed by numbers
#358 and 246
#Input: [5, 3, 0, 7, 4]
#Output: 82
#The minimum sum is formed by numbers
#35 and 047

arr.sort()
n = len(arr)
a = 0
b = 0
for i in range(n):
	if i%2 == 0:
		a = a*10 + arr[i]
	else:
		b = b*10 + arr[i]

print(a+b)
