n,q = map(int,input().split())
s = str(input())


def function(l,r):
    test = s[l-1:r]

#print(test)
    test  = list(test)
    unique_list = []
     
    # traverse for all elements
    for x in test:
            # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


    ff = []
#print(unique_list)

    for i in range(len(unique_list)):
        index = alphabet.index(unique_list[i])
        ff.append(index+1)

    
#print(ff)

    tt = []

    for i in range(len(unique_list)):
        cnt = test.count(unique_list[i])
        tt.append(cnt)

#print(tt)

    product = []

    for i ,j in zip(ff,tt):
        product.append(i*j)

#print(product)

    ans = sum(product)
    return ans
for i in range(q):
    l,r = map(int,input().split())
    print(function(l,r))
