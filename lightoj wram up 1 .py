from traceback import print_tb


t = int(input())
for i in range(1,t+1):
    a,b = map(int,input().split())
    res = a+b
    print(f"Case {i}: {res}")
    



