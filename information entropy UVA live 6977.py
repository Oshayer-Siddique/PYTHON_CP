import math
print("Information entropy")
def Information_entropy(digit,base,data):
	sum = 0
	for i in range(len(data)):
		sum = sum + (data[i]/100)*math.log(100/data[i],base)
	return sum

digit = int(input("digit = "))
base  = int(input("base = "))
data = list(map(int,input("\n enter the number").strip().split()))[:digit]

print(Information_entropy(digit,base,data))
