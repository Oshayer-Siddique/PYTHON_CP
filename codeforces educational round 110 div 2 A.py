t = int(input())
while t > 0:
    a,b,c,d = map(int,input().split())
    final1 = max(a,b)
    final2 = max(c,d)
    first_max = max(a,b,c,d)
    arr = [a,b,c,d]
    arr.sort()
    second_max = arr[-2]
    list1 = [first_max,second_max]
    list2 = [final1,final2]
    list1.sort()
    list2.sort()
    if list1 == list2:
        print("YES")
    else:
        print("NO")
    t  = t-1

