def func(n):
    if n == 1 or n == 2:
        return 1
    else:
        return func(n-1)+func(n-2)

n = int(input())
print(func(n))
    
def func1():
    print("HHH")
    return
    
func1()

def func2():
    print("JJJ")
    return func2()

func2()

import itertools
for j in range(8):
    for i in itertools.combinations([1, 2, 3,4,5,6,7], j):
        print(i)

import itertools
for i in itertools.permutations([1,2,3]):
    print(i)