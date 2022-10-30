
def findsubarray(arr):
    hasmap = {}

    out = []
    sum1 = 0

    for i in range(n):
        sum1 += arr[i]
    
    
        if sum1 == 0:
            out.append((0,i))
        
        al = []
    
        if sum1 in hasmap:
            al = hasmap.get(sum1)
            for j in range(len(al)):
                out.append((al[j]+1,i))
    
        al.append(i)
        hasmap[sum1] = al
        
    return out

def printoutput(output):
    for i in output:
        print ("Subarray found from Index " +
                str(i[0]) + " to " + str(i[1]))
        

n = int(input())
arr = list(map(int,input().strip().split()))[:n]

out = findsubarray(arr)

if len(out) == 0:
    print("No sub array")
else:
    printoutput(out)
    
    
    
    

