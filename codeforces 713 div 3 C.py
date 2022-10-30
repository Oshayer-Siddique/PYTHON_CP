t = int(input())
while t > 0:
    def isPalindrome(str):
 
    # Run loop from 0 to len/2
        for i in range(0, int(len(str)/2)):
            if str[i] != str[len(str)-i-1]:
                return False
        return True
 
    
 
    a,b = map(int,input().split())
    s = str(input())
    arr = list(s)
    n = len(arr)
    y = 0
    if a == 1 and b == 0 and s == '?':
        print('0')
    else:
        for k in range(n):
            if arr[n-k-1] == '?' and  arr[k] == '0':
                arr[n-k-1] = '0'
            elif arr[n-k-1] == '1' and arr[k] == '0':
                y = 0
            elif arr[n-k-1] == '?' and arr[k] == '1':
                arr[n-k-1] = '1'
            elif arr[n-k-1] == '0' and arr[k] == '1':
                y = 1 
 
        #print(*arr,sep="")
        zero ,one = 0,0
        for i in range(n):
            if arr[i] == '0':
                zero+=1
            elif arr[i] == '1':
                one += 1
 
        a1 = a - zero
        b1 = b - one
        #print(a1,b1)
        if a1 % 2 == 1 and b1 % 2 == 1:
            y = 1
        if b1 >0:
            for k in range(n):
                if arr[k] == '?':
                    arr[k] = arr[n-k-1] = '1'
                    b1 = b1 - 2
                    if b1 <= 0:
                        break
        if a1 > 0:
            for k in range(n):
                if arr[k] == '?':
                    arr[k] = arr[n-k-1] = '0'
                    a1 = a1-2
                    if a1 <=  0:
                        break
        ans = isPalindrome(arr)
        #print(a1,b1)
        if y == 1:
            print(-1)
        elif arr.count('0') != a or arr.count('1') != b:
            print(-1)
        elif isPalindrome(arr) == False:
            print(-1)
        
 
        else:
            print(*arr,sep="")
    t = t-1