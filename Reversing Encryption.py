n = int(input())
string = str(input())

arr = []
for j in range(2,n+1,+1):
    if n % j == 0:
        arr.append(j)

def reverse(string ,l ,h):
    string = list(string)

    while( l <h):
        temp = string[l]
        string[l] = string[h]
        string[h] = temp

        l = l+ 1
        h = h - 1
    return "".join(string)



for i in range(len(arr)):
    cur = reverse(string, 0, arr[i] - 1)
    string = cur

print(string)



