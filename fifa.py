 t = int(input())
while t > 0:
    string = str(input())
    pat = '123'


 
    len1 = len(string)
    len2 = len(pat)

    
 
    hash_pat = [0] * 256
    hash_str = [0] * 256
 
    for i in range(len2):
        hash_pat[ord(pat[i])] +=1
    start ,start_index ,min_len = 0, -1 , float('inf')
    count = 0
    for j in range(len1):
        hash_str[ord(string[j])] += 1

        if hash_str[ord(string[j])] <= hash_pat[ord(string[j])]:
            count +=1
        if count == len2:
            while (hash_str[ord(string[start])] >hash_pat[ord(string[start])] or hash_pat[ord(string[start])] == 0):
                if hash_str[ord(string[start])] > hash_pat[ord(string[start])]:
                    hash_str[ord(string[start])] -= 1
                    start +=1
            len_window = j - start + 1
            if min_len > len_window:
                min_len = len_window
                start = start_index

    if start_index == -1:
        print(0)
    else:
        print(min_len)
    t = t-1
