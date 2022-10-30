print("Generate all binary digit")


def printarr(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")
    print()


def generate_binary(arr, n, i):
    if i == n:
        printarr(arr, n)
        return
    else:

        arr[i] = 0
        generate_binary(arr, n, i + 1)

        arr[i] = 1
        generate_binary(arr, n, i + 1)


n = int(input("n = "))
arr = [None] * n
i = 0
generate_binary(arr, n, i)
