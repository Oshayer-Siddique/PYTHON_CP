print("Uvalive 6844")

def factorial(p):
	if p == 0:
		return 1
	for i in range(1,p):
		p = p*i
	return p
def binomial_co(n,k):
	return factorial(n)//(factorial(n-k)*factorial(k))

while(True):
	count = 0
	L = []
	low = int(input("low = "))
	high = int(input("high = "))
	while(low<=high):
		for i in range(0,low+1,+1):
			L.append(binomial_co(low,i))
		low = low+1

	for i in range(len(L)):
		if L[i] % 2 != 0:
			count = count+1

	print(count)
