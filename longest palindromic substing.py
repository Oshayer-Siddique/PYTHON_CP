s = str(input())
'''n = len(s)
maxlen = 0
start = 0
for i in range(n):
    for j in range(i,n):
        flag = 1
        for k in range(0,((j-i)//2),+1):
            if s[i+k] != s[j-k]:
                flag = 0
        
        if flag == 1 and (j-i+1) > maxlen:
            start = i
            maxlen = j - i + 1'''
low ,high = map(int,input().split())
def printall(s,low,high):
    for i in range(low,high+1):
        print(s[i],end=" ")


