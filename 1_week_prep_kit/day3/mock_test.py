def palindromeIndex(s):
    # Write your code here
    if s == s[::-1]: return -1
    s_len = len(s)

    for i in range(s_len//2):
        if s[i] != s[s_len-1-i]:
            if s[i:s_len-1-i] == s[i:s_len-1-i][::-1]:
                return s_len-1-i
            elif s[i+1:s_len-i] == s[i+1:s_len-i][::-1]:
                return i
    return -1



    #return index

if __name__ == '__main__':
   
    s = "baa"

    result = palindromeIndex(s)
    print(result)

