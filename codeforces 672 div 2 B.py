print("Codeforces Round #672 (Div. 2 .B)")


def combi(arr, temp, i, k):
    if i > len(arr) - 1:
        if len(temp) == k:
            if (temp[0] & temp [1]) >= (temp[0] ^ temp[1]):
                print(temp)


        return

    else:
        temp.append(arr[i])
        combi(arr, temp, i + 1, k)

        #while i < len(arr) - 1 and arr[i] == arr[i + 1]:
            #i = i + 1

        temp.pop()
        combi(arr, temp, i + 1, k)


t = int(input())
for testcase in range(t):
    n = int(input())
    arr =  list(map(int,input().strip().split()))[:n]
    k = 2
    temp = []
    i = 0

    combi(arr,temp,i,k)
