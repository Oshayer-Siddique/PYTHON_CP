print("Pattern Searching")
#Naive Algorithm
txt = "AAAAABAABABABABAAABABA"
pat = "AABA"

for i in range(len(txt)-len(pat)+1):
	j = 0
	while(j<len(pat)):
		if txt[i+j] != pat[j]:
			break
		j = j+1
	if (j == len(pat)):
		print("pattern found at = ",i)

print("Naive Algorithm")
txt = "aaabababa"
patt = "ab"
for i in range(len(txt)-len(patt)+1):
	for j in range(len(patt)):
		if(txt[i+j] != patt[j]):
			break
		j = j+1
	if j == len(patt):
		print(i)
