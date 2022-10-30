t = int(input())
while t > 0:
    string = str(input())
    pat = '123'
# Python3 program to find the smallest window
# containing all characters of a pattern.
 
# Function to find smallest window
# containing all characters of 'pat'

 
    len1 = len(string)
    len2 = len(pat)
 
    # Check if string's length is
    # less than pattern's
    # length. If yes then no such
    # window can exist
#if len1 < len2:
 
    #print("No such window exists")
    
 
    hash_pat = [0] * 256
    hash_str = [0] * 256
 
    # Store occurrence ofs characters of pattern
    for i in range(0, len2):
        hash_pat[ord(pat[i])] += 1
 
    start, start_index, min_len = 0, -1, 1000000000000000000
    
    # Start traversing the string
    count = 0  # count of characters
    for j in range(0, len1):
        
        # count occurrence of characters of string
        hash_str[ord(string[j])] += 1
    
        # If string's char matches with
        # pattern's char then increment count
        if (hash_str[ord(string[j])] <=hash_pat[ord(string[j])]):
            count += 1

        # if all the characters are matched
        if count == len2:
            #print("YES")

        # Try to minimize the window
            while (hash_str[ord(string[start])] >hash_pat[ord(string[start])] or hash_pat[ord(string[start])] == 0):
                
                if (hash_str[ord(string[start])] > hash_pat[ord(string[start])]):
                    hash_str[ord(string[start])] -= 1
                    start += 1
 
            # update window size
            len_window = j - start + 1
            if min_len > len_window:
                
                min_len = len_window
                start_index = start
 
    # If no window found
    if start_index == -1:
        print(0)

    else:
        print(min_len)
 
    t = t-1

 


