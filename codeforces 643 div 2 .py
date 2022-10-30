print("codeforces 643 A")


def digits(n):
    largest = 0
    smallest = 0
    while (n):
        r = n % 10
        largest = max(r, largest)
        smallest = min(r, smallest)
        n = n // 10
    print(largest, smallest)


n = int(input("n = "))
digits(n)
