t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    arr.sort()
    arr.reverse()
    alice = 0
    bob = 0
    for i in range(n):
        if i % 2 == 0:
            if arr[i] % 2 == 0:
                alice += arr[i]
        elif i % 2 == 1:
            if arr[i] % 2 == 1:
                bob += arr[i]

    if alice> bob:
        print("Alice")
    elif alice == bob:
        print("Tie")
    else:
        print("Bob")
    t = t-1